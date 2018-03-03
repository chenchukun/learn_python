from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from Model import *
from contextlib import contextmanager
from threading import Thread

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
DBSession = sessionmaker(bind=engine, autocommit=False)

# scoped_session默认使用线程本地数据存储，且多次实例化将得到相同的对象，除非调用remove()
Session = scoped_session(DBSession)

@contextmanager
def session_scope():
    session = DBSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def newSession():
    with session_scope() as session:
        for i in range(10):
            users = session.query(User).all()
            print(users)

def scopeSession():
    global Session
    Session = scoped_session(DBSession)
    session1 = Session()
    session2 = Session()
    print('session1 == session2' if session1==session2 else 'session1 != session2')
    Session.remove()
    session2 = Session()
    print('session1 == session2' if session1 == session2 else 'session1 != session2')
    for i in range(10):
        users = session2.query(User).all()
        print(users)

def main():
    threads = []
    for i in range(4):
        t = Thread(target=newSession)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    threads = []
    for i in range(4):
        t = Thread(target=scopeSession)
        t.start()
        threads.append(t)
    session = Session()
    for i in range(10):
        users = session.query(User).all()
        print(users)

    for t in threads:
        t.join()



if __name__ == '__main__':
    main()