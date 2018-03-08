from gevent import monkey
monkey.patch_all()
import gevent
import requests
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import time

def request(url):
    resp = requests.get(url)
#    print(resp.status_code)



def testGevent(url, num):
    start = time.time()
    gevent.joinall([ gevent.spawn(request, url) for i in range(num) ])
    end = time.time()
    print('Gevent {} requests, spend {} s'.format(num, end - start))


def testSeq(url, num):
    start = time.time()
    for i in range(num):
        request(url)
    end = time.time()
    print('Sequential {} requests, spend {} s'.format(num, end - start))

def testThread(url, num):
    start = time.time()
    for i in range(num):
        t = Thread(target=request, args=(url,))
        t.start()
    end = time.time()
    print('MultiThread {} requests, spend {} s'.format(num, end - start))


def testThreadPool(url, num):
    start = time.time()
    executor = ThreadPoolExecutor(4)
    for i in range(num):
        executor.submit(partial(request, url))
    executor.shutdown()
    end = time.time()
    print('ThreadPool {} requests, spend {} s'.format(num, end - start))

if __name__ == '__main__':
    url = 'https://www.baidu.com'
    num = 1000
    testThread(url, num)
    testThreadPool(url, num)
    testGevent(url, num)
    testSeq(url, num)