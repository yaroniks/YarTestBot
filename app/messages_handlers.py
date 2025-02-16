import app.keyboards as kb
from aiogram import types, F, Router

router = Router()

@router.message(F.text == 'ping')
async def ping(message: types.Message):
    await message.answer('pong')

@router.message(F.text == 'Боты Яровича')
async def bots(message: types.Message):
    await message.answer('Боты Яровича:', reply_markup=kb.mine_bots)
