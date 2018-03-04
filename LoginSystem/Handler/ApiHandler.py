from tornado.web import RequestHandler
import bcrypt
from Model.DBSession import DBSession
from Model.Model import *
import json
from sqlalchemy.orm import scoped_session
from contextlib import contextmanager
import re
import logging
import uuid
import time
from com import Jwt


class ApiHandler(RequestHandler):
    postReqs = {'login', 'register'}
    getReqs = {'search'}

    Session = scoped_session(DBSession)

    userNameRe = '[a-zA-z]\\w{0,9}'
    emailRe = '^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    passwordRe = '.{6,16}'

    @contextmanager
    def __getSession(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise

    def post(self, req):
        if req not in self.postReqs:
            self.set_status(404)
            self.render('404.html')
        else:
            self.__handler(req)

    def get(self, req):
        if req not in self.getReqs:
            self.set_status(404)
            self.render('404.html')
        else:
            self.__handler(req)

    def __handler(self, req):
        try:
            info = getattr(self, req)()
            self.write(json.dumps(info))
        except Exception as e:
            retJson = {
                'retcode': -1,
                'retmsg': str(e)
            }
            self.write(json.dumps(retJson))
            logging.exception(e)

    def login(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        email = self.get_argument('email').strip()
        password = self.get_argument('password').strip()
        self.__loginCheck(email, password)
        session = self.Session()
        auth = session.query(EmaliAuth).filter(EmaliAuth.email==email).first()
        if not auth:
            raise Exception('邮箱未注册')
        hash = bcrypt.hashpw(password.encode(), auth.password.encode()).decode()
        if auth.password != hash:
            raise Exception('密码错误')
        user = session.query(User).filter(User.uid == auth.uid).one()
        user.last_login_time = now
        session.add(user)
        info = {'email': email, 'uid': user.uid, 'username': user.username}
        token = Jwt.genToken(86400, info)
        info['token'] = token
        self.set_cookie('token', token)
        return {'retcode': 0, 'retmsg': '登录成功', 'info': info}


    def register(self):
        username = self.get_argument('username').strip()
        email = self.get_argument('email').strip()
        password = self.get_argument('password').strip()
        self.__registerCheck(username, email, password)

        hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        uid = str(uuid.uuid1())
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        user = User(username=username, register_time=now, uid=uid)
        auth = EmaliAuth(password=hash, email=email, uid=user.uid)
        with self.__getSession() as session:
            session.add(user)
            session.add(auth)
        return {'retcode': 0, 'retmsg': '注册成功，请登录', 'info': {'email': email, 'uid': uid, 'username': username}}

    def __registerCheck(self, username, email, password):
        if not re.match(self.userNameRe, username):
            raise Exception('用户名不合法')
        if not re.match(self.emailRe, email):
            raise Exception('邮箱地址不合法')
        if not re.match(self.passwordRe, password):
            raise Exception('密码不合法')
        session = self.Session()
        auth = session.query(EmaliAuth).filter(EmaliAuth.email == email).all()
        if auth:
            raise Exception('邮箱地址已被注册')

    def __loginCheck(self, email, password):
        if not re.match(self.emailRe, email):
            raise Exception('邮箱地址不合法')
        if not re.match(self.passwordRe, password):
            raise Exception('密码不合法')

    def search(self):
        token = self.get_cookie('token')
        info = Jwt.parseToken(token)
        return {'retcode': 0, 'retmsg': '查询成功', 'data': '测试数据......'}


