import aiogram
import asyncio
import logging
from helpful import *
from aiogram import Bot, Dispatcher
from app.buttons_handlers import router as r1
from app.commands_handlers import router as r2
from app.messages_handlers import router as r3

logging.basicConfig(level=logging.INFO)
bot = Bot(config.bot_token)
dp = Dispatcher()

async def main():
    dp.include_routers(r1, r2, r3)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
