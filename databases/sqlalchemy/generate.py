import faker
from Model import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
import sys

gen = faker.Factory.create()

users = [User(uid = gen.random_int(), username=gen.word(), register_time=gen.date_time(),
    sex = random.choice(['男', '女']), birth=gen.date(), location=gen.city(),
    headimgurl=gen.image_url(), status=0) for i in range(10)]

print(users)
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')

DBSession = sessionmaker(bind=engine)

session = DBSession()

session.add_all(users)
session.commit()

session.close()