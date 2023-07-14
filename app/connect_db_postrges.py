from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import asyncio
import redis.asyncio as rd
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from app.main import settings

Base = declarative_base()

class Users(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)



async def postgersconn():
  engine = create_engine(settings.postgers)
  Session = sessionmaker(bind=engine)
  Base.metadata.create_all(engine)
  return Session()

session = postgersconn()
