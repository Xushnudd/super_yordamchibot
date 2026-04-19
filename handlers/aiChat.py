from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states.states import BotStates

from keyboards.keyboards import back_menu

router = Router()

@router.message(F.text == "AI bilan suhbat")
async def message(m: types.Message, state: FSMContext):
    await state.set_state(BotStates.aiMode)
    await m.answer("AI rejimiga o'tdingiz. Savolingizni yozing.", reply_markup=back_menu)

@router.message(BotStates.aiMode)
async def handleAiChat(m: types.Message):
    await m.answer(f"AI javobi: Siz {m.text} dedingiz", reply_markup=back_menu)