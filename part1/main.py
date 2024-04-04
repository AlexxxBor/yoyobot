from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6811149083:AAHNClb9ZhuDO8-pTp0Q2yaqjFpiB2VFBDU')
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
