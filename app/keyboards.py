from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

def create_reply_markup(data: list[str], resize: bool = True, one_time: bool = False) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=i) for i in data]], resize_keyboard=resize, one_time_keyboard=one_time)


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Боты Яровича'), KeyboardButton(text='ping')],
], resize_keyboard=True)

bot_info_default = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Понятно.', callback_data='main_page')],
    [InlineKeyboardButton(text='Оставить отзыв', callback_data='make_feedback')]
])

mine_bots = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='РКСИ Планшетка', callback_data='plansbot'),
     InlineKeyboardButton(text='Журнал ИС',  callback_data='rksibot')],
    [InlineKeyboardButton(text='YarTestBot', callback_data='testbot')]
])
