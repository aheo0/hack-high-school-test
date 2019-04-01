import sqlite3

with sqlite3.connect('sampldsf') as connection:
    c = connection.cursor()
    c.execute('''
        DROP TABLE  IF EXISTS users
    ''')
    c.execute('''
        CREATE TABLE users(
            id INTEGER PRIMARY KEY autoincrement,
            username TEXT,
            password TEXT
        )
    ''')

    c.execute('''
        INSERT INTO users VALUES (
            ('hello', 'hello'),
            ('admin', 'admin')
        )
    ''')

