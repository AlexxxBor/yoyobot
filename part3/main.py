from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv  # для загрузки данных из .env файлов
import os  # для чтения .env файлов

load_dotenv()  # загрузка данных из .env

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """ Обработчик команды /start """
    # Отправка стикера в ответ
    await message.answer_sticker('CAACAgIAAxkBAAMOZg66G6_YECeqI869EbX9EtKQsFQAAmgRAAKFjyhJydwtNZ-SPOk0BA')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать!')


# Обратотка документов, стикеров и прочих вложений, которые можно отправлять и
# получать с помощью тг бота
@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    """ Обработчик сообщения со стикером """

    # Вернёт в ответ на личное сообщение id стикера
    await message.answer(message.sticker.file_id)

    # Добавить в группу бота и назначить его админом
    # ответит на сообщение со стикером, отправленное в группу
    # при этом отправит сообщение пользователю, приславшему стикер id чата,
    # где он работает
    await bot.send_message(message.from_user.id, message.chat.id)


@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    """ Обработчик документов и фотографий """
    # forward_message пересылает сообщение message.message_id в группу
    # с id (-4152521677) от юзера message.from_user.id
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id,
                              message.message_id)


@dp.message_handler()
async def answer(message: types.Message):
    """ Обработчик неизвестного сообщения (любого, кроме известных) """
    await message.reply('Я тебя не понимаю.')


if __name__ == "__main__":
    executor.start_polling(dp)
