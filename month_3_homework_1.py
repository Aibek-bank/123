"""Техническое задание: Бот на aiogram 3
Общие требования:
Фреймворк: aiogram 3.x
Библиотеки: aiogram, asyncio

1. Стартовое меню:
После старта бота пользователю должно быть предложено два варианта:

Камен, ножницы, бумага
1. Игра "Камен, ножницы, бумага":
Пользователь выбирает :

Камень
Ножницы
Бумага

Бот случайным образом выбирает одно из тех же действий (камень, ножницы или бумага).
После выбора пользователю показывается результат (победа, поражение или ничья).

Доп Задание:
 Запушить проект в гитхаб
 Скрыт токен"""

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import random
import token

bot = Bot(token=token)
dp = Dispatcher()

choices = ("Камень", "Ножницы", "Бумага")

@dp.message(Command("game"))
async def game(message: types.Message):
    await message.answer("Выберите камень, ножницы или бумагу:")

@dp.message()
async def play_game(message: types.Message):
    user_choice = message.text.strip()

    if user_choice not in choices:
        return await message.answer("Пожалуйста, выберите одно из трех слов: Камень, Ножницы или Бумага")

    bot_choice = random.choice(choices)

    if user_choice == bot_choice:
        result = "Ничья"
    elif (
        (user_choice == "Камень" and bot_choice == "Ножницы") or
        (user_choice == "Ножницы" and bot_choice == "Бумага") or
        (user_choice == "Бумага" and bot_choice == "Камень")
    ):
        result = "Победа"
    else:
        result = "Поражение"

    await message.answer(f"Ты выбрал: {user_choice}\nБот выбрал: {bot_choice}\n{result}")
    await message.answer("Если хотите сыграть снова, напишите команду /game.")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
