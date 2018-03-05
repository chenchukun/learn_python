from concurrent.futures import ThreadPoolExecutor
import time

def sleep(n):
    print('sleep start')
    time.sleep(n)
    print('sleep finish')
    return n

if __name__ == '__main__':
    # 创建大小为4的线程池
    executor = ThreadPoolExecutor(4)
    # 将任务放入线程池队列
    f1 = executor.submit(sleep, 5)
    f2 = executor.submit(sleep, 5)
    f3 = executor.submit(sleep, 5)
    # 判断任务是否完成
    print('f1.done() = ', f1.done())
    print('f2.done() = ', f2.done())
    print('f3.done() = ', f3.done())
    print('main start')
    time.sleep(7)
    # 获取任务执行结果
    print('f1.done() = ', f1.done(), 'f1.result() = ', f1.result())
    print('f2.done() = ', f2.done(), 'f1.result() = ', f1.result())
    print('f3.done() = ', f3.done(), 'f1.result() = ', f1.result())
    print('main finish')