import pytest
import asyncio
import redis.asyncio as rd
from app.main import settings

@pytest.fixture(scope="module")
@pytest.mark.asyncio
async def redisconnet():
  yield await rd.from_url(settings.redis)
  await asyncio.gather(
      test_set_get(redisconnet),
       test_incr(redisconnet),
       test_delete(redisconnet)
  )
  redisconnet().flushall()

async def test_set_get(redisconnet):
    await redisconnet.set('key', 'value')
    result = await redisconnet.get('key')
    assert result == b'value'

async def test_incr(redisconnet):
    await redisconnet.set('counter', 0)
    await redisconnet.incr('counter')
    result = redisconnet.get('counter')
    assert int(result) == 1

async def test_delete(redisconnet):
    await redisconnet.set('key', 'value')
    await redisconnet.delete('key')
    result = await redisconnet.get('key')
    assert result is None
