import os
import asyncio
from dotenv import load_dotenv

from fastapi import FastAPI, Request

from aiogram import Bot, Dispatcher
from aiogram.types import Update

from handlers import start, aiChat, pdfCreate

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = FastAPI()

dp.include_router(start.router)
dp.include_router(aiChat.router)
dp.include_router(pdfCreate.router)

@app.post("/bots/super_yordamchibot/")
async def webhook(request: Request):
    data = await request.json()
    update = Update(**data)
    
    await dp.feed_update(bot, update)
    return {"ok": True}