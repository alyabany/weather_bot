# bot.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from config import Token_bot as TOKEN
from core.handlers.start import register_handlers



async def main():
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    )

    dp = Dispatcher(storage=MemoryStorage())

    register_handlers(dp)

    print("Bot is running...")
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())