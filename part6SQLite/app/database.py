import sqlite3 as sq

db = sq.connect('tg.db')  # если файла нет, он создаётся
cur = db.cursor()  # для запросов к БД

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
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
