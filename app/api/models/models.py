from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
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


class UserAndPassword(BaseModel):
    username: str
    password: str

class SignInRequestModel(UserAndPassword):
    pass


class SignUpRequestModel(UserAndPassword):
    email: str
    name: str
    last_name: str


class UserUpdateRequestModel(UserAndPassword):
    email: str
    name: str
    last_name: str


class UsersListResponse(BaseModel):
    users: list(User)
