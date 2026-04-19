from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states.states import BotStates

from keyboards.keyboards import back_menu

router = Router()

@router.message(F.text == "PDF qilish")
async def message(m: types.Message, state: FSMContext):
    await state.set_state(BotStates.pdfMode)
    await m.answer("Pdf tayyorlash uchun rasmlaringizni yuboring !", reply_markup=back_menu)