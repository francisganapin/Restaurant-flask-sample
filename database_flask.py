import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DateTimeSelection (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            select_date TEXT,
            select_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()
