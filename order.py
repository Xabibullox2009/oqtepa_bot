from aiogram import types, F, Router
from buttons.button_main import rt
from aiogram.types import ReplyKeyboardRemove
from buttons.inline_btn import inline_btn
from buttons.buttons import delivery_keyboard, approve_location , location,contact

rt = Router()

@rt.message(F.text == "🛒Buyurtma berish")
async def order_handler(message: types.Message):
    await message.answer("Buyurtma berish bo'limiga xush kelibsiz! Quyidagi menyudan kerakli bo'limni tanlang.", reply_markup=delivery_keyboard)

@rt.message(F.text == "🛵Доставка")
async def delivery_handler(message: types.Message):
    await message.answer("Siz yetkazib berish xizmatini tanladingiz. Iltimos, manzilingizni yuboring.")
    await message.answer("📍Joylashuvni yuborish", reply_markup=location)

@rt.message(F.location)
async def location_handler(message: types.Message):
    await message.answer("Joylashuvingiz qabul qilindi. Iltimos, tasdiqlang.", reply_markup=approve_location)
    await message.answer("Siz yuborgan joylashuv:", reply_markup=ReplyKeyboardRemove())
    await message.answer_location(latitude=message.location.latitude, longitude=message.location.longitude)
    if approve_location:
        await message.answer("Joylashuvingiz tasdiqlandi. Buyurtmangizni davom ettiring.", reply_markup=inline_btn)

@rt.message(F.text == "🚶Самовывоз")
async def pickup_handler(message: types.Message):
    await message.answer("Siz o'z joyingizdan olib ketish xizmatini tanladingiz. Iltimos, manzilingizni yuboring." , reply_markup=location)

@rt.message(F.text == "🔙Назад")
async def back_handler(message: types.Message):
    await message.answer("Asosiy menyuga qaytdingiz.", reply_markup=inline_btn)
