from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command='help', description='Справка по работе бота'),
        BotCommand(command='cat', description='Случайно изображение кота'),
        BotCommand(command='dog', description='Случайное изображение собаки'),
        BotCommand(command='fox', description='Случайное изображение лисы'),
        BotCommand(command='capybara', description='Случайное изображение капибары'),
        BotCommand(command='panda', description='Случайное изображение панды')
    ]
    await bot.set_my_commands(commands=commands)
