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
