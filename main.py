import aiogram
import asyncio
import logging
from helpful import *
from aiogram import Bot, Dispatcher
from app import *

logging.basicConfig(level=logging.INFO)
bot = Bot(config.bot_token)
dp = Dispatcher()

async def main():
    dp.include_routers(r1, r2, r3, r4)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
