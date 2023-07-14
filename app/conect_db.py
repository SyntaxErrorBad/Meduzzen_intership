from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import asyncio
import redis.asyncio as rd
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values


env_values = dotenv_values('.env')

async def redisconnet():
  return await rd.from_url(env_values.get('POSTGRES'))


Base = declarative_base()

class Users(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)



async def postgersconn():
  engine = create_engine('postgresql://admin:123456@postgres:5432/postgres')
  Session = sessionmaker(bind=engine)
  Base.metadata.create_all(engine)
  return Session()


redis = redisconnet()
session = postgersconn()
