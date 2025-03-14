import config
import app.keyboards as kb
import app.database.requests as req
from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router()


class FeedBack(StatesGroup):
    bot = State()
    stars = State()
    text = State()


@router.callback_query(F.data == 'make_feedback')
async def make_feedback_query(callback: types.CallbackQuery, state: FSMContext):
    data = callback.message.text.split(' ')[-1]

    has_feedback = await req.has_review(callback.from_user.id, data)
    if has_feedback:
        return await callback.answer('Вы уже оставили отзыв на данного бота.', show_alert=True)

    await state.set_state(FeedBack.stars)
    await state.update_data(bot=data)
    await callback.message.edit_text(f'*Отзыв на {config.bots[data]}*\nВыберите оценку.', parse_mode='MARKDOWN')
    await callback.message.answer('Выберите оценку.',
                                  reply_markup=kb.create_reply_markup([f'{i} ⭐' for i in range(1, 6)], one_time=True))
    await callback.answer('Выберите оценку.')


@router.message(FeedBack.stars)
async def stars_message(message: types.Message, state: FSMContext):
    try:
        stars = int(message.text[0])
    except:
        return await message.answer('Не удалось понять оценку.', reply_markup=kb.main)
    await state.update_data(stars=stars)
    await state.set_state(FeedBack.text)
    await message.answer('Отправьте текст отзыва.')


@router.message(FeedBack.text)
async def text_message(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await req.save_review(message.from_user.id, data['bot'], data['stars'], data['text'])
    await message.answer('Спасибо за ваш отзыв.', reply_markup=kb.main)
    await state.clear()
