import helpful.keyboards as kb
from aiogram import types, F, Router

router = Router()

@router.message(F.text == 'ping')
async def ping(message: types.Message):
    await message.answer('pong')


@router.message(F.text == 'Боты яровича')
async def bots(message: types.Message):
    await message.answer('Боты яровича', reply_markup=kb.mine_bots)
