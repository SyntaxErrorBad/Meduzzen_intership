import pytest
import asyncio
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people1'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

@pytest.fixture(scope="module")
@pytest.mark.asyncio
async def PostgersConn():
  engine = create_engine('postgresql://admin:123456@postgres:5432/postgres')
  Session = sessionmaker(bind=engine)
  Base.metadata.create_all(engine)
  yield Session()


async def test_create_table(PostgersConn):
    assert 'people1' in get_table_list(PostgersConn)

async def get_table_list(PostgersConn):
    result = PostgersConn.execute(text("SELECT people FROM information_schema.tables WHERE table_schema='public'"))
    return [row[0] for row in result.fetchall()]