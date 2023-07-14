import pytest
import asyncio
import redis.asyncio as rd

@pytest.fixture(scope="module")
@pytest.mark.asyncio
async def RedisConnet():
  redis = await rd.from_url("redis://redis:6379")
  yield redis
  await asyncio.gather(
      test_set_get(RedisConnet),
       test_incr(RedisConnet),
       test_delete(RedisConnet)
  )
  redis.flushall()

async def test_set_get(RedisConnet):
    await RedisConnet.set('key', 'value')
    result = await RedisConnet.get('key')
    assert result == b'value'

async def test_incr(RedisConnet):
    await RedisConnet.set('counter', 0)
    await RedisConnet.incr('counter')
    result = RedisConnet.get('counter')
    assert int(result) == 1

async def test_delete(RedisConnet):
    await RedisConnet.set('key', 'value')
    await RedisConnet.delete('key')
    result = await RedisConnet.get('key')
    assert result is None
