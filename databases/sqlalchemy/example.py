from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import *
from sqlalchemy import and_, func, text

# 创建引擎，相当于保存数据库连接信息的对象
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')

# 使用engine的连接信息创建一个Session类，此时不会连接数据库，需要实例化为对象
DBSession = sessionmaker(bind=engine)
# 修改Session绑定的引擎
#DBSession.configure(bind=engine)


# 创建session对象，可以使用engine先创建连接，并将Session对象绑定到该连接上，也可以直接创建Session
# 此时不会发起与数据库的连接，而是在使用该session的时候再进行连接
conn = engine.connect()
session = DBSession(bind=conn)

#session = DBSession()


# 相当于select * from users
users = session.query(User).all()
print(users)

# select * from users where sex = '男' order by uid
users = session.query(User).filter(User.sex == '男').order_by(User.uid).all()
print(users)

# 对于复制查询，可以直接使用sql语句
users = session.execute('select users.uid, username, sex from users join local_auth on users.uid = local_auth.uid')
for user in users:
    print(user)

# select sex from users group by sex
group = session.query(User.sex, func.count(User.sex)).group_by(User.sex).all()
print(group)

# select username, location from users where location like 'North%'
users = session.query(User.username, User.location).filter(User.location.like('North%')).all()
print(users)

# select * from users where uid in ('147', '148)
users = session.query(User).filter(User.uid.in_(['147', '148'])).all()
print(users)

# select * from users where uid like '2%' and sex='男' limit 1
users = session.query(User).filter(and_(User.uid.like('2%'), User.sex=='男')).first()
print(users)

# select * from users where uid = '7377'   one()指明结果有且只有一行，若没结果或结果不止一行将报错
users = session.query(User).filter(User.uid == '7377').one()
print(users)

# select * from users where year(register_time) = 2003 and sex = '男'
users = session.query(User).filter(text('year(register_time) = 2003 and sex = "男"')).all()
print(users)

user = session.query(User).filter(User.uid == '7377').one()
print(user)

user.last_login_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
session.add(user)

user = session.query(User).filter(User.uid == '7377').one()
print(user)

user = session.query(User).filter(User.uid == 'jjjjjf').all()
print(user)

session.commit()

session.close()