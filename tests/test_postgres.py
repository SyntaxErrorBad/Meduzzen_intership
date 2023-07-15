import pytest
import asyncio
from sqlalchemy import create_engine, Column, Integer, String, text, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.main import settings


Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

@pytest.fixture(scope="module")
@pytest.mark.asyncio
async def postgersconn():
    engine = create_engine(settings.postgres)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    metadata = MetaData(bind=engine)
    metadata.drop_all(bind=engine)


async def test_create_table(postgersconn):
    assert 'person' in get_table_list(postgersconn)

async def get_table_list(postgersconn):
    result = postgersconn.execute(text("SELECT person FROM information_schema.tables WHERE table_schema='public'"))
    return [row[0] for row in result.fetchall()]
