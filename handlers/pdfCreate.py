import os
import time
import shutil

import asyncio
from PIL import Image

from aiogram import Bot, Router, types, F
from aiogram.fsm.context import FSMContext

from states.states import BotStates

from keyboards.keyboards import pdf_menu, main_menu

from utils.pdfGenerate import pdfGenerate

router = Router()

@router.message(F.text == "PDF qilish")
async def start_pdf_mode(m: types.Message, state: FSMContext):
    await state.set_state(BotStates.pdfMode)
    await m.answer('Pdf tayyorlash uchun rasmlaringizni yuboring va "Tayyor ✅" tugmasini bosing !', reply_markup=pdf_menu)
    
@router.message(BotStates.pdfMode, F.photo)
async def collect_photos(m: types.Message, state: FSMContext):
    data = await state.get_data()
    
    now = time.time()
    last_activity = data.get("last_activity", now)
    
    if now - last_activity > 300:
        await state.update_data(photo_ids=[m.photo[-1].file_id], last_activity=now)
        await m.answer("Avvalgi yuborgan rasmlaringiz vaqti o'tib ketgani uchun o'chirildi. Yangi PDF boshlandi.")
    
    photoList = data.get("photo_ids", [])
    photoList.append(m.photo[-1].file_id)
    await state.update_data(photo_ids=photoList)
    
@router.message(BotStates.pdfMode, F.text == "Tayyor ✅")
async def handle_pdf_finish(m: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    photoList = data.get("photo_ids", [])
    if not photoList:
        await m.answer("Rasm yubormadingiz")
        return
    
    await m.answer("PDF tayyorlanmoqda...")
    user_dir = str(m.from_user.id)
    os.makedirs(user_dir, exist_ok=True)
    
    imgs = []
    for i, f_id in enumerate(photoList):
        img = f"{user_dir}/{i}.jpg"
        await bot.download(f_id, destination=img)
        imgs.append(img)
        
    pdf_file = f"{user_dir}/Document.pdf"
    
    images = []
    for path in imgs:
        with Image.open(path) as img:
            images.append(img.convert("RGB"))
            
    await asyncio.to_thread(
        images[0].save,
        pdf_file,
        format="PDF",
        save_all=True,
        append_images=images[1:]
    )
        
    await m.answer_document(
        document=types.FSInputFile(pdf_file),
        caption="Tayyor",
        reply_markup=main_menu
    )
    
    await state.clear()
    for img in images:
        img.close()
    images.clear()
    shutil.rmtree(user_dir)