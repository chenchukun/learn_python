from concurrent.futures import ThreadPoolExecutor
import time
import threading
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
DBSession = sessionmaker(bind=engine, autocommit=False)
Session = scoped_session(DBSession)

def test():
    time.sleep(0.1)
    session = Session()
    print(threading.current_thread().getName(), session)

if __name__ == '__main__':
    executor = ThreadPoolExecutor(2)
    executor.submit(test)
    executor.submit(test)
    executor.submit(test)
    executor.submit(test)
    executor.submit(test)
