from collections import deque
from tornado import ioloop
import logging

class TimeWheel(object):

    def __init__(self, users, timeout=10):
        self.__users = users
        self.__timeout = timeout
        self.__wheel = deque([set() for i in range(timeout)])
        ioloop.IOLoop.current().call_later(1, self.check)
        logging.info('TimeWheel init: timeout = {}'.format(timeout))

    def check(self):
        users = self.__wheel.popleft()
        self.__wheel.append(set())
        for user in users:
            if user in self.__users:
                logging.info('[{}] timeout TimeWheel close connection'.format(user.request.remote_ip))
                user.close()
        ioloop.IOLoop.current().call_later(1, self.check)

    def push(self, user):
        for users in self.__wheel:
            try:
                users.remove(user)
            except:
                pass
        self.__wheel[len(self.__wheel) - 1].add(user)
