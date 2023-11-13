import asyncio
import requests

def dummy_request():
  return requests.get('https://httpbin.org/basic-auth/user/pass', auth('user', 'pass'))

async def async_dummy_request():
  return requests.get('https://httpbin.org/basic-auth/user/pass', auth('user', 'pass'))

def main():
  d1 = dummy_requst()
  d2 = dummy_requst()
  
async def async_main():
  d1 = await async_dummy_requst()
  d2 = await async_dummy_requst()

async def async_main_together():
  d = await asyncio.gather(*[async_dummy_requst(), async_dummy_requst()])