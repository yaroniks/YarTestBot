from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

def create_reply_markup(data: list[str]) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=i) for i in data]], resize_keyboard=True)


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='ping'), KeyboardButton(text='Боты яровича')],
], resize_keyboard=True)

bot_info_default = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Понятно.', callback_data='main_page')]
])

mine_bots = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='РКСИ Планшетка', callback_data='plansbot'),
     InlineKeyboardButton(text='Журнал ИС',  callback_data='rksibot')],
    [InlineKeyboardButton(text='YarTestBot', callback_data='testbot')]
])
