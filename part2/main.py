from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv  # для загрузки данных из .env файлов
import os  # для чтения .env файлов

load_dotenv() # загрузка данных из .env
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """ Обработчик команды /start """
    await message.answer(f'{message.from_user.first_name}, добро пожаловать!')


@dp.message_handler()
async def answer(message: types.Message):
    """ Обработчик неизвестного сообщения (любого, кроме известных) """
    await message.reply('Я тебя не понимаю.')


if __name__ == "__main__":
    executor.start_polling(dp)
