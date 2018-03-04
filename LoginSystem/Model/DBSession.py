from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

__engine = create_engine('mysql+pymysql://root:123456@localhost:3306/search_system?charset=utf8')

DBSession = sessionmaker(bind=__engine, autocommit=False)
