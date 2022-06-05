import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')

    f = open('sql_dump/schema.sql', 'r' ) 
    conn.executescript(f.read())

    f = open('sql_dump/dump.sql')
    conn.executescript(f.read())

    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn 