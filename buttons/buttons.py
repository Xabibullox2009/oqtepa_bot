from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

delivery_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛵Доставка"), KeyboardButton(text="🚶Самовывоз")],
        [KeyboardButton(text="🔙Назад")]
    ],
    resize_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Raqamni yuborish", request_contact=True)],
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Joylashuvni yuborish", request_location=True)],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

approve_location = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅Ha"), KeyboardButton(text="❌Yo'q")]
    ],
    resize_keyboard=True
)