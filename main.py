import config
import asyncio
import logging
from app import *
from aiogram import Bot, Dispatcher
from app.database.models import async_main

logging.basicConfig(level=logging.INFO)


async def main():
    await async_main()

    bot = Bot(config.bot_token)
    dp = Dispatcher()
    dp.include_routers(r1, r2, r3, r4)
    try:
        await dp.start_polling(bot)
    except:
        pass


if __name__ == '__main__':
    asyncio.run(main())
