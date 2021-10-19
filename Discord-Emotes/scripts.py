import requests, aiohttp

async def request(url):
 async with aiohttp.ClientSession() as cs:
  async with cs.get(url) as r:
    data = r.json()
    return data['url']
   
async def smug():
 return await request("https://nekos.life/api/v2/img/smug")


async def hug():
  return await request('https://nekos.life/api/v2/img/hug')


async def kiss():
  return await request('https://nekos.life/api/kiss')


async def pat():
  return await request('https://nekos.life/api/v2/img/pat')

async def poke():
 return await request('https://nekos.life/api/v2/img/poke')

async def slap():
  return await request('https://nekos.life/api/v2/img/slap')

async def tickle():
  return await request('https://nekos.life/api/v2/img/tickle')


async def neko():
  return await request('https://nekos.life/api/neko')


async def ngif():
  return await request('https://nekos.life/api/v2/img/ngif')

async def cuddle():
  return await request('https://nekos.life/api/v2/img/cuddle')