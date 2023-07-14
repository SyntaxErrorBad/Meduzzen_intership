from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import asyncio
import redis.asyncio as rd
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

from conect_db import redis, session, Users


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)



@app.get("/")
async def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }

@app.get("/users")
async def health_users():
    await redis.set("Fkey","Fvalue")
    result = session.query(Users).all()
    value = await redis.get("Fkey")
    return {
        "status_code": 201,
        "detail": "Ok",
        "result": {
            "SQLAlchemy" : result,
            "Redis" : value.decode()
        }
    }
    
