from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv  # для загрузки данных из .env файлов
import os  # для чтения .env файлов

# Импорт виртуальной клавиатуры
from aiogram.types import ReplyKeyboardMarkup

load_dotenv()  # загрузка данных из .env
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


# Создаём клавиатуры для обычного пользователя и для админа
# Переменная с именем клавиатуры
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)  # пустая клавиатура
# Наполнение клавиатуры для обычного пользователя
main_kb.add('Каталог').add('Корзина').add('Контакты')  # добавим кнопки

# Клавиатура для админа с кнопкой админки
main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')

# Клавиатура админ-панели
admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')

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

    # Проверка id администратора и вывод админ клавиатуры
    # Такую же проверку нужно добавить в обработчик "Админ-панель"
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        # int(os.getenv('ADMIN_ID')) для преобразования содержимого из .env
        await message.answer(f'Вы авторизовались как администратор!',
                             reply_markup=main_admin)


# ==Обработчик для кнопок с клавиатуры для обычного пользователя== #
@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    """Обработчик кнопки 'Каталог'"""
    await message.answer(f'Каталог пуст!')


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
