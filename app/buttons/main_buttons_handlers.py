import app.keyboards as kb
from aiogram import types, F, Router
from aiogram.types import InlineKeyboardButton

router = Router()


@router.callback_query(F.data == 'main_page')
async def main_page_query(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Боты Яровича:', reply_markup=kb.mine_bots)


@router.callback_query(F.data == 'plansbot')
async def plansbot_query(callback: types.CallbackQuery):
    await callback.answer('Выбрано: РКСИ Планшетка')
    markup = kb.bot_info_default.__deepcopy__()
    markup.inline_keyboard[0].append(InlineKeyboardButton(text='Ссылка', url='https://t.me/RKSIplanshetkabot'))
    await callback.message.edit_text('*РКСИ Планшетка*\n'
                                     'Бот, который парсит пары кабинетов, групп, преподавателей из планшетки первого и второго корпусов.\n'
                                     'Уведомления об изменениях, архивирование планшеток.\n'
                                     f'Обозначение: {callback.data}',
                                     parse_mode='MARKDOWN', reply_markup=markup)


@router.callback_query(F.data == 'rksibot')
async def rksibot_query(callback: types.CallbackQuery):
    await callback.answer('Выбрано: Журнал ИС')
    markup = kb.bot_info_default.__deepcopy__()
    markup.inline_keyboard[0].append(InlineKeyboardButton(text='Ссылка', url='https://t.me/RKSIjournalbot'))
    await callback.message.edit_text('*Журнал ИС*\n'
                                     'Бот, который парсит оценки и пропуски с журналов групп ИС-11 и ИС-12.\n'
                                     f'Обозначение: {callback.data}',
                                     parse_mode='MARKDOWN', reply_markup=markup)


@router.callback_query(F.data == 'testbot')
async def testbot_query(callback: types.CallbackQuery):
    await callback.answer('Выбрано: YarTestBot')
    markup = kb.bot_info_default.__deepcopy__()
    markup.inline_keyboard[0].append(InlineKeyboardButton(text='GitHub', url='https://github.com/yaroniks/YarTestBot'))
    await callback.message.edit_text('*YarTestBot*\n'
                                     'Тестовый Open Source телеграм бот с новой архитектурой на Python с ипользованием: Aiogram, SQLAlchemy, Dotenv.\n'
                                     f'Обозначение: {callback.data}',
                                     parse_mode='MARKDOWN', reply_markup=markup)
