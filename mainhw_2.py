"""Техническое задание: Информационный Telegram-бот
Цель
Создать Telegram-бот, предоставляющий пользователям информацию на заданные темы или запросы.
Функционал
Команда /start:
1.Приветствие пользователя.
2.Краткое описание возможностей бота.
3.Вывод меню с кнопками для выбора тем.
Информационное меню:
1.Отображение списка тем или разделов через кнопки (ReplyKeyboardMarkup).
2.Темы/разделы (пример):
1.Новости.
2.Курсы валют.
3.Контактная информация.
4.Часто задаваемые вопросы (FAQ).
Предоставление информации:
1.Пользователь выбирает тему → бот отправляет заранее подготовленную информацию.
2.Пример:
1.Новости: "Сегодня: курс доллара вырос на 2%, акции падают."
2.Контакты: "Наша почта: info@example.com. Телефон: +123456789."
3.Курсы валют: "Доллар: 85₽, Евро: 90₽."
3.Информация придумайте сами какие либо вопросы но главное чтобы работало.
Дополнительные команды:
1./help: Описание всех доступных функций бота.
2./about: Краткая информация о проекте или боте.
3./menu: Вывод основного меню.

Доп задание: 
 Скрыт токен 
 Сделать без помощи ментора"""


from config import token
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

bot = Bot(token=token)
dp = Dispatcher()

keybord_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Новости')],
        [KeyboardButton(text='Курсы валют')],
        [KeyboardButton(text='Контактная информация')],
        [KeyboardButton(text='Часто задаваемые вопросы')],
        [KeyboardButton(text='/help'), KeyboardButton(text='/about')]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Привет! Добро пожаловать. Я помогу вам получить информацию. Выберите одну из тем.",
        reply_markup=keybord_main
    )

@dp.message(Command("help"))
async def help(message: types.Message):
    help_text = (
        "Этот бот предоставляет информацию по следующим темам:\n"
        "1. Новости\n"
        "2. Курсы валют\n"
        "3. Контактная информация\n"
        "4. Часто задаваемые вопросы\n\n"
        "Выберите тему из меню или напишите команду '/start' для начала."
    )
    await message.answer(help_text, reply_markup=keybord_main)

@dp.message(Command("about"))
async def about(message: types.Message):
    about_text = (
        "Этот бот создан для предоставления информации по различным темам, "
        "таким как новости, курсы валют и контактные данные. Используйте меню для выбора темы."
    )
    await message.answer(about_text, reply_markup=keybord_main)

@dp.message(lambda message: message.text == 'Новости')
async def news(message: types.Message):
    await message.answer("Сегодня: курс доллара вырос на 2%, акции падают.", reply_markup=keybord_main)

@dp.message(lambda message: message.text == 'Курсы валют')
async def exchange_rates(message: types.Message):
    await message.answer("Доллар: 85₽, Евро: 90₽.", reply_markup=keybord_main)

@dp.message(lambda message: message.text == 'Контактная информация')
async def contact_info(message: types.Message):
    await message.answer("Наша почта: info@example.com. Телефон: +123456789.", reply_markup=keybord_main)

@dp.message(lambda message: message.text == 'Часто задаваемые вопросы')
async def faq(message: types.Message):
    await message.answer("Вопрос: Как узнать актуальные курсы валют?\nОтвет: Используйте команду 'Курсы валют'.", reply_markup=keybord_main)

async def main():
    print("Запуск бота")
    await dp.start_polling(bot)

asyncio.run(main())
