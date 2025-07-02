import asyncio, os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from .keyboard_buttons.button import uz_menu, ru_menu, en_menu, til_uz, til_ru, til_en

bot = Bot(token='')

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f"Assalomu alaykum {message.from_user.first_name},"
                         "Московская пицца Доставка botiga xush kelibsiz!", reply_markup=uz_menu)

@dp.message(F.text == "Tilni o'zgartirish")
async def change_uz(message: Message):
    await message.answer("Tilni tanlang", reply_markup=til_uz)

@dp.message(F.text == "Изменить язык")
async def change_uz(message: Message):
    await message.answer("Выберите язык", reply_markup=til_ru)

@dp.message(F.text == "Change the language")
async def change_uz(message: Message):
    await message.answer("Select a language", reply_markup=til_en)
"""Til"""
@dp.message(F.text == "🇺🇿 O'zbek tili")
async def menu_uz(message: Message):
    await message.answer(f"Assalomu alaykum {message.from_user.first_name},"
                         "Московская пицца Доставка botiga xush kelibsiz!", reply_markup=uz_menu)

@dp.message(F.text == "🇺🇸 English")
async def menu_uz(message: Message):
    await message.answer(f"Hello {message.from_user.first_name},"
                         "welcome to the Московская пицца Доставка bot!", reply_markup=en_menu)

@dp.message(F.text == "🇷🇺 Русский язык")
async def menu_uz(message: Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name},"
                         "добро пожаловать в бот Московская пицца Доставка!", reply_markup=ru_menu)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot is running...")
    asyncio.run(main())
