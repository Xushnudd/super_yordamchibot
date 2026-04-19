from aiogram import Router, types, F
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext

from keyboards.keyboards import main_menu

router = Router()

@router.message(CommandStart())
@router.message(F.text == "🔝Bosh sahifa")
async def start(m: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()
    
    reply = f"Salom <a href='tg:user?id={m.from_user.id}'>{m.from_user.first_name} {m.from_user.last_name}</a>. Kerakli bo'limni tanlang !"
    await m.answer(reply, parse_mode="html", reply_markup=main_menu)