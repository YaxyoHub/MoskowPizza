from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

uz_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Menyu', web_app=WebAppInfo(url="https://google.com"))],
        [KeyboardButton(text="Tilni o'zgartirish"), KeyboardButton(text='CHat', web_app=WebAppInfo(url="https://google.com"))],
        [KeyboardButton(text='Mening buyurtmalarim', web_app=WebAppInfo(url="https://google.com"))]
    ],
    # resize_keyboard=True,
    resize_keyboard=False,
    one_time_keyboard=True
)

ru_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Меню', web_app=WebAppInfo(url="https://google.com"))],
        [KeyboardButton(text="Изменить язык"), KeyboardButton(text='Чать', web_app=WebAppInfo(url="https://google.com"))],
        [KeyboardButton(text='Мои заказы', web_app=WebAppInfo(url="https://google.com"))]
    ],
    # resize_keyboard=True,
    resize_keyboard=False,
    one_time_keyboard=True
)

en_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Menu', web_app=WebAppInfo(url="https://google.com"))],
        [KeyboardButton(text="Change the language"), KeyboardButton(text='Chat', web_app=WebAppInfo(url="https://google.com"))],
        [KeyboardButton(text='My orders', web_app=WebAppInfo(url="https://google.com"))]
    ],
    # resize_keyboard=True,
    resize_keyboard=False,
    one_time_keyboard=True
)
"""Tillar"""
til_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🇺🇸 English')],
        [KeyboardButton(text="🇺🇿 O'zbek tili")],
        [KeyboardButton(text='🇷🇺 Русский язык')]
    ],
    resize_keyboard=False,
    input_field_placeholder="Tilni tanlang",
    one_time_keyboard=True
)

til_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🇺🇸 English')],
        [KeyboardButton(text="🇺🇿 O'zbek tili")],
        [KeyboardButton(text='🇷🇺 Русский язык')]
    ],
    resize_keyboard=False,
    input_field_placeholder="Выберите язык",
    one_time_keyboard=True
)

til_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🇺🇸 English')],
        [KeyboardButton(text="🇺🇿 O'zbek tili")],
        [KeyboardButton(text='🇷🇺 Русский язык')]
    ],
    resize_keyboard=False,
    input_field_placeholder="Select a language",
    one_time_keyboard=True
)
