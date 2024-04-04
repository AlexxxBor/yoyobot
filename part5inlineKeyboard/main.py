from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv  # для загрузки данных из .env файлов
import os  # для чтения .env файлов

# Импорт обычной клавиатуры
from aiogram.types import ReplyKeyboardMarkup
# Импорт инлайн-клавиатуры к инлайн-кнопками
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()  # загрузка данных из .env
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add('Каталог').add('Корзина').add('Контакты')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')

# Создание инлайн-клавиатуры
# row_width кол-во кнопок в ряду
catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Футболки', url='https://ya.ru/'),
                 InlineKeyboardButton(text='Шорты', url='https://www.google.com/'),
                 InlineKeyboardButton(text='Кросовки', url='https://www.yahoo.com/'))
# далее добавить клавиатуру в Каталог
# Inline клавиатуры передают callback data боту на обработку или перебрасывают
# пользователя на url адрес

@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    """ Узнать свой ID """
    await message.answer(f'{message.from_user.id}')

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """ Обработчик команды /start """
    await message.answer_sticker('CAACAgIAAxkBAAMOZg66G6_YECeqI869EbX9EtKQsFQAAmgRAAKFjyhJydwtNZ-SPOk0BA')
    await message.answer(f'{message.from_user.first_name},'
                         f'добро пожаловать!', reply_markup=main_kb)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!',
                             reply_markup=main_admin)


# ==Обработчик для кнопок с клавиатуры для обычного пользователя== #
@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    """Обработчик кнопки 'Каталог'"""
    # Прикрепление клавиатуры к ответу
    await message.answer(f'Каталог пуст!', reply_markup=catalog_list)


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
        await message.answer(f'Администрировать', reply_markup=admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')


@dp.message_handler()
async def answer(message: types.Message):
    """ Обработчик неизвестного сообщения (любого, кроме известных) """
    await message.reply('Я тебя не понимаю.')


if __name__ == "__main__":
    executor.start_polling(dp)
