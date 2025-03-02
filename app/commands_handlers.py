import app.keyboards as kb
from aiogram import types, Router
import app.database.requests as req
from aiogram.filters.command import Command, CommandStart

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await req.add_chat(message.chat.id)
    await message.answer('Start', reply_markup=kb.main)


@router.message(Command('help'))
async def help(message: types.Message):
    await message.answer('Help')
