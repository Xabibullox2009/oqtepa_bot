import asyncio
import logging
from aiogram import Bot, Dispatcher , types
from aiogram.fsm.storage.memory import MemoryStorage
from config import settings
from buttons.button_main import rt
from registration import rtr

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = settings.BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(storage=MemoryStorage())



dp.include_router(rt)
dp.include_router(rtr)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())