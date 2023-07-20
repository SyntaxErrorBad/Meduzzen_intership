from app.config import settings
import asyncio
import redis.asyncio as rd


async def redisconnet():
  return await rd.from_url(settings.REDIS)



redis = redisconnet()