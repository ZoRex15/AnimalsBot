from aiogram import Bot, Dispatcher

import asyncio

from config.config import Config, load_config

from handlers.user_handlers import router
from keyboards.set_menu import set_commands



async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(router)
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    