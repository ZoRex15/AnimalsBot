import aiohttp


async def get_url_cat_photo():
    url = 'https://api.thecatapi.com/v1/images/search'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
            return res[0]['url']

async def get_url_dog_photo():
    url = 'https://dog.ceo/api/breeds/image/random'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
            return res['message']

async def get_url_capybara_photo():
    url = 'https://api.capy.lol/v1/capybara?json=true'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
    return res['data']['url']

async def get_url_panda_photo():
    url = 'https://some-random-api.com/animal/panda'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
            return res['image']

async def get_url_fox_photo():
    url = 'https://some-random-api.com/animal/fox'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
            return res['image']
