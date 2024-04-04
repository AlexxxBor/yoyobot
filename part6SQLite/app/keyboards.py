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
catalog_list.add(InlineKeyboardButton(text='Футболки', url='https://ya.ru/'),
                 InlineKeyboardButton(text='Шорты', url='https://www.google.com/'),
                 InlineKeyboardButton(text='Кросовки', url='https://www.yahoo.com/'))