import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Таблица пользователей
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (user_id INTEGER PRIMARY KEY, balance INTEGER, click_power INTEGER)''')
    # Таблица рефералов
    cursor.execute('''CREATE TABLE IF NOT EXISTS referals 
                      (referrer_id INTEGER, user_id INTEGER)''')
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users VALUES (?, 0, 1)", (user_id,))
    conn.commit()
    conn.close()