import redis
import time
import functools
from threading import Thread

class Producer(object):
    def __init__(self, host, port, password, db):
        self._conn = redis.StrictRedis(host=host, port=port, password=password, db=db)

    def send(self, topic, msg):
        dataKey = '_redismq_data_{}_'.format(topic)
        self._conn.rpush(dataKey, msg)


class Consumer(Thread):
    def __init__(self, host, port, password, db):
        Thread.__init__(self)
        self._conn = redis.StrictRedis(host=host, port=port, password=password, db=db)
        self.daemon = True
        self._exit = False

    def subscribe(self, topic, group, cb):
        self._topic = topic
        self._group = group
        self._callback = cb
        self.start()

    def close(self):
        self._exit = True

    def run(self):
        sha = self._conn.script_load('''
            local offset = redis.call('hget', KEYS[1], KEYS[2])
            offset = offset and offset or 0; 
            local msgs = redis.call('lrange', KEYS[3], offset, offset+KEYS[4])
            redis.call('hincrby', KEYS[1], KEYS[2], table.getn(msgs)) 
            return msgs''')
        groupKey = '_redismq_group_{}_'.format(self._topic)
        dataKey = '_redismq_data_{}_'.format(self._topic)
        while not self._exit:
            msgs = self._conn.evalsha(sha, 4, groupKey, self._group, dataKey, 10)
            for msg in msgs:
                self._callback(msg.decode())
            if not msgs:
                time.sleep(0.1)




def testProducer():
    producer = Producer('localhost', 6379, 'myredis', 1)
    while True:
        data = input('input: ')
        producer.send(data.split('----')[0], data.split('----')[1])

def testConsumer():
    def test(num, topic, msg):
        print(num, 'recv :', topic, msg)
    f1 = functools.partial(test, 1, 'test_topic')
    f2 = functools.partial(test, 2, 'test_topic')
    f3 = functools.partial(test, 3, 'test_topic')
    consumer1 = Consumer('localhost', 6379, 'myredis', 1)
    consumer1.subscribe('test_topic', 'test_group', f1)
    consumer2 = Consumer('localhost', 6379, 'myredis', 1)
    consumer2.subscribe('test_topic', 'test_group', f2)
    consumer3 = Consumer('localhost', 6379, 'myredis', 1)
    consumer3.subscribe('test_topic', 'test2_group', f3)


if __name__ == '__main__':
    testConsumer()
    testProducer()
