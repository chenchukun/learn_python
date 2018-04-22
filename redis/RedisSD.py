import redis
import time
from threading import Thread
from threading import Lock

class Register(Thread):
    def __init__(self, host, port, password, db):
        Thread.__init__(self)
        self.daemon = True
        self._conn = redis.StrictRedis(host=host, port=port, password=password, db=db)
        self._services = []
        self._lock = Lock()

    def register(self, srvname, srvdata):
        self._lock.acquire()
        self._services.append((srvname, srvdata))
        self._lock.release()


    def run(self):
        while True:
            self._lock.acquire()
            services = self._services
            self._lock.release()
            for item in services:
                self._conn.set('_redissd_{}'.format(item[0]), item[1], ex=10)
            time.sleep(5)

class Discovery(object):
    def __init__(self, host, port, password, db):
        self._conn = redis.StrictRedis(host=host, port=port, password=password, db=db)

    def discovery(self, srvname):
        keys = self._conn.keys('_redissd_{}*'.format(srvname))
        services = []
        for key in keys:
            value = self._conn.get(key)
            services.append(value.decode())
        return services


def testRegister():
    r = Register('localhost', 6379, 'myredis', 1)
    r.register('login', '{"srvname": "login", "ip": "localhost", "port": 6180}')
    r.start()
    r.register('game', '{"srvname": "game", "ip": "localhost", "port": 6181}')

def testDiscovery():
    d = Discovery('localhost', 6379, 'myredis', 1)
    while True:
        services = d.discovery('login')
        print('login: ', services)
        services = d.discovery('game')
        print('game: ', services)
        services = d.discovery('test')
        print('test: ', services)
        time.sleep(3)


if __name__ == '__main__':
    testRegister()
    testDiscovery()