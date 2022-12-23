from keyboards.default.keyboards import Til, Orqaga, Viloyatlar, start, Sozlamalar, Vaqt
from loader import dp
from aiogram.dispatcher.filters.builtin import Text
from aiogram import types

@dp.message_handler(Text(contains='start'))
async def bot_start(message: types.Message):
    await message.answer("Sizga kerak tugmani bosing yoki hudud nomini kiriting!",reply_markup=start)

@dp.message_handler(Text(contains='Til'))
async def bot_start(message: types.Message):
    await message.answer("Kerakli tilni tanlang",reply_markup=Til)


@dp.message_handler(Text(contains='Orqaga'))
async def bot_start(message: types.Message):
    await message.answer("Bosh sahifaga o'tildi",reply_markup=Orqaga)

@dp.message_handler(Text(equals=('Viloyatlar')))
async def bot_start(message: types.Message):
    await message.answer("Viloyatni tanlang",reply_markup=Viloyatlar)

@dp.message_handler(Text(contains='Sozlamalar'))
async def bot_start(message: types.Message):
    await message.answer("Sozlamalarga o'tildi",reply_markup=Sozlamalar)

@dp.message_handler(Text(contains='Vaqt'))
async def bot_start(message: types.Message):
    await message.answer("O'zingizga qulay vaqtni tanlang !\n"
                         "shu vaqtda ob-havo ma'lumotlari yuboriladi",reply_markup=Vaqt)



