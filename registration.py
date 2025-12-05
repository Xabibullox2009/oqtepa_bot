from aiogram import types,F
from aiogram.filters import Command
from buttons.buttons import contact
from buttons.inline_btn import inline_btn
from state import Registration
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.types import ReplyKeyboardRemove
rtr = Router()
from database import insert_user , get_all_users


@rtr.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.full_name
    user = get_all_users(user_id)
    if user:
        await message.answer(f"Qaytganingiz uchun rahmat {user[0][1]}!" , reply_markup=inline_btn)
    else:
        await message.answer(f"""Assalomu alaykum! Botga xush kelibsi, {username}
    Oldin ro'yxatdan o'ting""")
        await message.answer("Ismingizni kiriting: ")
        await state.set_state(Registration.name)

@rtr.message(Registration.name)
async def name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon nomeringizni yuboring:" , reply_markup=contact)
    await state.set_state(Registration.phone_number)

@rtr.message(Registration.phone_number,F.contact)
async def contact_handler_contact(message: types.Message , state: FSMContext):
    phone = message.contact.phone_number
    await state.update_data(phone_number=phone)
    data = await state.get_data()
    name = data.get("name")
    user_id = message.from_user.id
    insert_user(user_id, name, phone)
    await message.answer("Registratsiya jarayonidan muvaffaqiyatli o'tdingiz!", reply_markup=ReplyKeyboardRemove())
    await message.answer("""Buyurtma berishni boshlash uchun 🛒
Buyurtma qilish tugmasini bosing\n
Oqtepa lavash menu""" ,reply_markup=inline_btn)