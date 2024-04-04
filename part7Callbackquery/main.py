from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv  # для загрузки данных из .env файлов
import os  # для чтения .env файлов

# Импорт клавиатур из файла app.py
from app import keyboards as kb
# Импорт базы данных из database.py
from app import database as db

# CRUD - Create, Read, Update, Delete
# Рефакторинг кода (раскидать файлы по папкам)

load_dotenv()  # загрузка данных из .env
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


async def on_startup(_):
    """Ф-ция запускается при запуске бота, добавляется в on_startup executor"""
    await db.db_start()
    print('Бот успешно запущен.')


@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    """ Узнать свой ID """
    await message.answer(f'{message.from_user.id}')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """ Обработчик команды /start """
    # Добавляем id пользователя в базу данных
    await db.cmd_start_db(message.from_user.id)
    await message.answer_sticker('CAACAgIAAxkBAAMOZg66G6_YECeqI869EbX9EtKQsFQAAmgRAAKFjyhJydwtNZ-SPOk0BA')
    await message.answer(f'{message.from_user.first_name},'
                         f'добро пожаловать!', reply_markup=kb.main_kb)  # kb.
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!',
                             reply_markup=kb.main_admin)  # kb.


# ==Обработчик для кнопок с клавиатуры для обычного пользователя== #
@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    """Обработчик кнопки 'Каталог'"""
    # .kb
    await message.answer(f'Каталог пуст!', reply_markup=kb.catalog_list)


@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    """Обработчик кнопки 'Контакты' """
    await message.answer(f'Корзина пуста!')


@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    """Обработчик текста 'Контакты' с кнопки"""
    await message.answer(f'Товары покупать у него: @mesudoteach')


# ==Обработчик для админа== #
@dp.message_handler(text='Админ-панель')
async def contacts(message: types.Message):
    """Обработчик кнопки Админ-панель; в env должна быть константа admin_id"""
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        # .kb
        await message.answer(f'Администрировать', reply_markup=kb.admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')


@dp.message_handler()
async def answer(message: types.Message):
    """ Обработчик неизвестного сообщения (любого, кроме известных) """
    await message.reply('Я тебя не понимаю.')


# Обработчики callback запросов
@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    """ Callback НЕ принимает message. CallbackQuery содержит ту же
    информацию, что и Message """
    user_id = callback_query.from_user.id
    match callback_query.data:
        case 't-shirt':
            await bot.send_message(chat_id=user_id, text='Вы выбрали футболки')
        case 'shorts':
            await bot.send_message(chat_id=user_id, text='Вы выбрали шорты')
        case 'sneakers':
            await bot.send_message(chat_id=user_id, text='Вы выбрали кроссовки')

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    # skip_updates позволяет...
