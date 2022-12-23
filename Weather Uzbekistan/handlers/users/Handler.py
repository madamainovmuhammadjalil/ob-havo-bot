from aiogram import types, executor
from aiogram.dispatcher.filters.builtin import CommandStart,CommandHelp
import datetime
import requests
import configparser
from loader import dp

adress=""
today=datetime.date.today().strftime("%d-%m-%y")

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!"'\n'
                         "Botga xush kelibsiz \n"
                         "Manzil nomini kiriting")


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler()
async def worktext(message: types.Message):
    try:
        global adress
        adress = message.text

        url = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=cf0ef5ba9e334592a5461627220208&q={adress}&aqi=no")
        response = url.json()['current']
        respons = url.json()['location']
        a=response['last_updated']
        a1='🔄'f"Oxirgi yangilanishi: {a}"
        b=response['temp_c']
        g=response['wind_mph']
        g1=f"💨 Shamol tezligi {g} m/s "


        c=respons['name']
        v=f"Nomi: {c}"
        d=respons['region']
        d1=f"Viloyat: {d}"
        e=respons['country']
        e1=f"Mamlakat: {e}"
        f=respons['localtime']


        j='C'

        c1=f"🕘 Sana {f}"
        c2= f"☀ Ob havo {b}{j}"


        cc=f"{a1}'\n'{c1}'\n'{e1}'\n'{d1}'\n'{v}'\n'{c2}'\n'{g1}"


        await message.answer(cc)



    except:
        await message.answer("Kiritilgan manzil nomi noto'g'ri! \n"
                             "Iltimos manzil nomini to'g'ri kiriting")


if __name__ == "main":
    executor.start_polling(dp, skip_updates=True)