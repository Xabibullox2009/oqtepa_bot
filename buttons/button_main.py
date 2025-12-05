from aiogram import Router, F, types
from .buttons import location

rt = Router()

@rt.message(F.text == "🛵Доставка")
async def delivery_handler(message: types.Message):
    await message.answer("Siz yetkazib berish xizmatini tanladingiz. Iltimos, manzilingizni yuboring.")
    await message.answer("📍Joylashuvni yuborish", reply_markup=location)

@rt.message(F.text == "🚶Самовывоз")
async def pickup_handler(message: types.Message):
    await message.answer("Siz o'z joyingizdan olib ketish xizmatini tanladingiz. Iltimos, manzilingizni yuboring." , reply_markup=location)