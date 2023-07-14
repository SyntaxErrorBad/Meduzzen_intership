from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import asyncio
import redis.asyncio as rd
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)


Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)



async def postgersconn():
  engine = create_engine('postgresql://admin:123456@postgres:5432/postgres')
  Session = sessionmaker(bind=engine)
  Base.metadata.create_all(engine)
  return Session()


async def redisconnet():
  return await rd.from_url("redis://redis:6379")



@app.get("/")
async def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }

@app.get("/users")
async def health_users():
    redis = await redisconnet()
    session = await postgersconn()
    await redis.set("Fkey","Fvalue")
    result = session.execute(text("SELECT * FROM people"))
    value = await redis.get("Fkey")
    return {
        "status_code": 201,
        "detail": "Ok",
        "result": {
            "SQLAlchemy" : result,
            "Redis" : value.decode()
        }
    }
