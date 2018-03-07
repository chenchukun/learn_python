import requests
from threading import Thread, Lock
from tornado import ioloop

ThreadNum = 10
requestNum = 10000
prev = 0
suc = 0
seconds = 0

lock = Lock()

def request():
    global suc
    for i in range(requestNum):
        resp = requests.post('http://127.0.0.1:6180/api/login',
            data = {'email':'chen_chukun@qq.com', 'password': '123456'})
        lock.acquire()
        suc += 1
        lock.release()

def stat():
    global usc, prev, seconds, ThreadNum, requestNum
    seconds += 1
    curr = suc
    add = curr - prev
    prev = curr
    if suc == (ThreadNum * requestNum):
        ioloop.IOLoop.current().stop()
        ioloop.IOLoop.current().close()
        print('Throughput: {} QPS'.format(suc / seconds))
        return
    print('QPS: {}'.format(add))
    ioloop.IOLoop.current().call_later(1, stat)

if __name__ == '__main__':
    for i in range(ThreadNum):
        t = Thread(target=request)
        t.start()
    ioloop.IOLoop.current().call_later(1, stat)
    ioloop.IOLoop.current().start()