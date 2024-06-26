import sqlite3 as sq

db = sq.connect('tg.db')  # если файла нет, он создаётся
cur = db.cursor()  # для запросов к БД

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "tg_id INTEGER, "
                "cart_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT, "
                "desc TEXT, "
                "price TEXT, "
                "photo TEXT, "
                "brand TEXT)")
    db.commit()


# Данную функцию нужно запускать при старте Бота
# В main.py создать on_startup()
async def cmd_start_db(user_id):
    user = cur.execute(f"SELECT * FROM accounts WHERE tg_id == {user_id}").fetchone()
    if not user:
        cur.execute(f"INSERT INTO accounts (tg_id) VALUES ({user_id})")
        db.commit()


# Добавление товара в БД
async def add_item(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO items (name, desc, price, photo, brand) VALUES (?, ?, ?, ?, ?)',
                    (data['name'], data['desc'], data['price'], data['photo'], data['type']))
        db.commit()
