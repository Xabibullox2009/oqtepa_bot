from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛒Buyurtma berish", callback_data="order")],
        [
            InlineKeyboardButton(text="ℹ️Biz haqimizda", callback_data="about_us"),
            InlineKeyboardButton(text="🛍️Buyurtmalarim", callback_data="my_orders")
        ],
        [InlineKeyboardButton(text="🏘️Filiallar", callback_data="branches")],
        [
            InlineKeyboardButton(text="✍️Fikr bildirish", callback_data="offer"),
            InlineKeyboardButton(text="⚙️Sozlamalar", callback_data="settings")
        ]
    ]
)
