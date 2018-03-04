from sqlalchemy import Column, INTEGER, String, Enum, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
import time

class User(declarative_base()):
    __tablename__ = 'users'

    uid = Column(String(48), primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    register_time = Column(DateTime, nullable=False)
    sex = Column(Enum('男', '女'), default='男')
    birth = Column(Date, default=None)
    location = Column(String(48), default='火星')
    last_login_time = Column(DateTime, default=None)
    headimgurl = Column(String(128))
    status = Column(INTEGER, default=0)

    def __repr__(self):
        return 'User(uid = {}, username = {}, register_time = {}, sex = {}, birth = {}, ' \
            'location = {}, last_login_time = {}, headimgurl = {}, status = {})'\
            .format(self.uid, self.username, self.register_time, self.sex, self.birth,
                self.location, self.last_login_time, self.headimgurl, self.status)


class EmaliAuth(declarative_base()):
    __tablename__ = 'email_auth'

    email = Column(String(48), primary_key=True)
    uid = Column(String(48), unique=True, nullable=False)
    password = Column(String(128), nullable=False)