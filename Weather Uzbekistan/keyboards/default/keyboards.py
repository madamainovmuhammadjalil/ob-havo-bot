from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

start=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Viloyatlar'),
            KeyboardButton(text="⚙️Sozlamalar"),
        ],
    ],
    resize_keyboard=True
)
Orqaga=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Viloyatlar'),
            KeyboardButton(text="⚙️Sozlamalar"),
        ],
    ],
    resize_keyboard=True
)
Til=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿O'zbekcha"),
            KeyboardButton(text="🇷🇺Руский"),
            KeyboardButton(text="🇬🇧English"),
        ],
        [
            KeyboardButton(text="⬅️Orqaga"),
        ],
    ],
    resize_keyboard=True
)
Viloyatlar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Urganch'),
        ],
        [
            KeyboardButton(text="Termiz"),
        ],
        [
            KeyboardButton(text="Jizzax"),
        ],
        [
            KeyboardButton(text="Toshkent"),
        ],
        [
            KeyboardButton(text="Namangan"),
        ],
        [
            KeyboardButton(text="Qarshi"),
        ],
        [
            KeyboardButton(text="Fergana"),
        ],
        [
            KeyboardButton(text="Andijon"),
        ],
        [
            KeyboardButton(text="Navoiy"),
        ],
        [
            KeyboardButton(text="Buxoro"),
        ],
        [
            KeyboardButton(text="Samarqand"),
        ],
        [
            KeyboardButton(text="Guliston"),
        ],
        [
            KeyboardButton(text="Nukus"),
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
        ]
    ],
)
Sozlamalar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔄Tilni o'zgartirish"),
        ],
        [
            KeyboardButton(text="🔄Shaharni o'zgartirish"),
        ],
        [
            KeyboardButton(text="🕰Vaqtni o'zgartirish"),
        ],
        [
            KeyboardButton(text="🚫Vaqtni o'chirish"),
        ],
[
            KeyboardButton(text="⬅️Orqaga qaytish"),
        ],

    ],
)
Vaqt=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="0:00"),
            KeyboardButton(text="1:00"),
            KeyboardButton(text="2:00"),
            KeyboardButton(text="3:00"),
        ],
[
            KeyboardButton(text="4:00"),
            KeyboardButton(text="5:00"),
            KeyboardButton(text="6:00"),
            KeyboardButton(text="7:00"),
        ],
[
            KeyboardButton(text="8:00"),
            KeyboardButton(text="9:00"),
            KeyboardButton(text="10:00"),
            KeyboardButton(text="11:00"),
        ],
[
            KeyboardButton(text="12:00"),
            KeyboardButton(text="13:00"),
            KeyboardButton(text="14:00"),
            KeyboardButton(text="15:00"),
        ],
[
            KeyboardButton(text="16:00"),
            KeyboardButton(text="17:00"),
            KeyboardButton(text="18:00"),
            KeyboardButton(text="19:00"),
        ],
[
            KeyboardButton(text="20:00"),
            KeyboardButton(text="21:00"),
            KeyboardButton(text="22:00"),
            KeyboardButton(text="23:00"),
        ],
        [
            KeyboardButton(text="⬅️Orqaga"),
        ],
    ],
)