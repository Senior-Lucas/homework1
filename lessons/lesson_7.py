import sqlite3


def create_tables(conn):
    conn.execute("""
    CREATE TABLE students  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)
def add_student(name, age, city,):
    conn.excute("""
    INSERT INTO students (name, age, city)
    VALUES (?, ?, ?)
    """)

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    create_tables(conn)


add_student('Igor', 30, 'Bishkek')