import os
import asyncio
from dotenv import load_dotenv

from aiohttp import web

from aiogram import Bot, Dispatcher
from aiogram.types import Update

from handlers import start, aiChat, pdfCreate

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(aiChat.router)
dp.include_router(pdfCreate.router)

# async def main():
#     await dp.start_polling(bot)
    
# if __name__ == "__main__":
#     asyncio.run(main())

async def handle(request):
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return web.Response(text="ok")

app = web.Application()
app.router.add_post("/webhook", handle)

if __name__ == "__main__":
    web.run_app(app, port=5000)