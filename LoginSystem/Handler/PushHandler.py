from tornado.websocket import WebSocketHandler
from com.TimeWheel import TimeWheel
import logging
from com import Jwt

class PushHandler(WebSocketHandler):

    TIMEOUT_SECOND = 45

    users = set()  # 用来存放在线用户的容器

    timeWheel = TimeWheel(users, TIMEOUT_SECOND)

    def open(self):
        token = self.get_cookie('token')
        try:
            info = Jwt.parseToken(token)
        except:
            logging.error('[{}] token = {} is invalid, close connection'.format(self.request.remote_ip, token))
            self.close()
        else:
            logging.info('[{}] connection add to users'.format(self.request.remote_ip))
            self.users.add(self)  # 建立连接后添加用户到容器中
            self.timeWheel.push(self)

    def on_message(self, message):
        logging.info('recv \'{}\' from [{}]'.format(message, self.request.remote_ip))
        self.timeWheel.push(self)
        if message == 'heartbeat':
            self.write_message(message)
            return

    def on_close(self):
        logging.info('[{}] close'.format(self.request.remote_ip))
        try:
            self.users.remove(self) # 用户关闭连接后从容器中移除用户
        except:
            pass