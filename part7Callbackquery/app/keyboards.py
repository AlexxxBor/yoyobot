from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add('Каталог').add('Корзина').add('Контакты')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')

# Создание инлайн-клавиатуры
# row_width кол-во кнопок в ряду
catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Футболки', callback_data='t-shirt'),
                 InlineKeyboardButton(text='Шорты', callback_data='shorts'),
                 InlineKeyboardButton(text='Кросовки', callback_data='sneakers'))

# callback data: callback это функция, которая передаётся на вход другой ф-ции
# чтобы она была запущена в ответ на какое-то событие
# Событие кнопки называется callback data
# Меняем url`ы кнопок на имена callback-событий, добавляем функции в БД
