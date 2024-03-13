from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import CommandStart, Command
from aiogram.types import URLInputFile

from keyboards.inline import create_another_photo
from service.service import (
    get_url_cat_photo,
    get_url_dog_photo,
    get_url_capybara_photo,
    get_url_panda_photo, 
    get_url_fox_photo
    )
from filters.filters import AnimallData


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    TEXT = f'''
Привет, {message.from_user.full_name}!

Я телеграм бот который генерирует случайные изображения животных.

Справку по работе бота можно посмотреть при помощи команды /help
'''
    await message.answer(text=TEXT)

@router.message(Command(commands=['help']))
async def help(message: Message):
    TEXT = '''
/cat - случайное изображение котика
/dog - случайное изображение собаки
/capybara - случайное изображение капибары
/panda - случайное изображение панды
/fox - случайное изображение лисы
'''
    await message.answer(text=TEXT)

@router.message(Command(commands=['cat']))
async def send_random_cat_image(message: Message):
    image = URLInputFile(url=get_url_cat_photo())
    await message.answer_photo(
        photo=image,
        reply_markup=create_another_photo(animal='cat')
    )

@router.message(Command(commands=['dog']))
async def send_random_cat_image(message: Message):
    image = URLInputFile(url=get_url_dog_photo())
    await message.answer_photo(
        photo=image,
        reply_markup=create_another_photo(animal='dog')
    )

@router.message(Command(commands=['capybara']))
async def send_random_cat_image(message: Message):
    image = URLInputFile(url=get_url_capybara_photo())
    await message.answer_photo(
        photo=image,
        reply_markup=create_another_photo(animal='capybara')
    )

@router.message(Command(commands=['panda']))
async def send_random_cat_image(message: Message):
    image = URLInputFile(url=get_url_panda_photo())
    await message.answer_photo(
        photo=image,
        reply_markup=create_another_photo(animal='panda')
    )

@router.message(Command(commands=['fox']))
async def send_fox_photo(message: Message):
    image = URLInputFile(url=get_url_fox_photo())
    await message.answer_photo(
        photo=image,
        reply_markup=create_another_photo(animal='fox')
    )
    
@router.callback_query(AnimallData(('cat', 'dog', 'capybara', 'panda', 'fox')))
async def another_photo(callback: CallbackQuery):
    animals = {
        'cat': get_url_cat_photo,
        'dog': get_url_dog_photo,
        'capybara': get_url_capybara_photo,
        'panda': get_url_panda_photo,
        'fox': get_url_fox_photo
    }
    url = animals[callback.data]()
    media = InputMediaPhoto(media=url)
    try:
        await callback.message.edit_media(
            media=media,
            reply_markup=create_another_photo(animal=callback.data)
        )
    except Exception as error:
        print(f'Произошла ошибка: {error}')
    finally:
        await callback.answer()