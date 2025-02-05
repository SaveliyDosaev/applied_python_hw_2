# Опять бесстыдно взято из лекции
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from middleware import LoggingMiddleware
from handlers import router
import asyncio

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.message.middleware(LoggingMiddleware())
dp.include_router(router)

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())