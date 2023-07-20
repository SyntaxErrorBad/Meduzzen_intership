from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List
from ...config import settings

Base = declarative_base()
engine = create_engine(settings.POSTGRES_MIG)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(255),nullable=False,unique=True)
    password = Column(String(255),nullable=False)
    email = Column(String(255),nullable=False,unique=True)
    name = Column(String(255),nullable=False)
    last_name = Column(String(255))


class SignInRequestModel(BaseModel):
    username: str
    password: str


class SignUpRequestModel(BaseModel):
    username: str
    password: str
    email: str
    name: str
    last_name: str


class UserUpdateRequestModel(BaseModel):
    username: str
    email: str
    name: str
    last_name: str


#class UsersListResponse(BaseModel):
    #users: List[User]
