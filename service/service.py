import requests


def get_url_cat_photo():
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url).json()
    return res[0]['url']

def get_url_dog_photo():
    url = 'https://dog.ceo/api/breeds/image/random'
    res = requests.get(url).json()
    return res['message']

def get_url_capybara_photo():
    url = 'https://api.capy.lol/v1/capybara?json=true'
    res = requests.get(url=url).json()
    return res['data']['url']

def get_url_panda_photo():
    url = 'https://some-random-api.com/animal/panda'
    res = requests.get(url=url).json()
    return res['image']

def get_url_fox_photo():
    url = 'https://some-random-api.com/animal/fox'
    res = requests.get(url=url).json()
    return res['image']
