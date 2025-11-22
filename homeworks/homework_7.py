import sqlite3

DATABASE_NAME = "library.db"
def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            number_of_pages INTEGER NOT NULL,
            number_of_copies INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Таблица 'books' успешно создана '{DATABASE_NAME}'.")


def insert_books():
    books_data = [
        (1, 'Война и мир', 'Лев Толстой', 1869, 'Роман-эпопея', 1300, 5),
        (2, 'Преступление и наказание', 'Федор Достоевский', 1866, 'Философский роман', 600, 3),
        (3, 'Мастер и Маргарита', 'Михаил Булгаков', 1966, 'Фантастический роман', 480, 8),
        (4, 'Отцы и дети', 'Иван Тургенев', 1862, 'Роман', 350, 4),
        (5, 'Евгений Онегин', 'Александр Пушкин', 1833, 'Роман в стихах', 250, 6),
        (6, 'Мертвые души', 'Николай Гоголь', 1842, 'Поэма в прозе', 300, 2),
        (7, 'Герой нашего времени', 'Михаил Лермонтов', 1840, 'Роман', 200, 7),
        (8, 'Архипелаг ГУЛАГ', 'Александр Солженицын', 1973, 'Документальный роман', 1500, 1),
        (9, '1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 320, 10),
        (10, 'Гарри Поттер и философский камень', 'Джоан Роулинг', 1997, 'Фэнтези', 400, 15),
        (11, 'Властелин колец: Братство кольца', 'Дж. Р. Р. Толкин', 1954, 'Фэнтези', 500, 12)
    ]

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', books_data)

    conn.commit()
    conn.close()
    print(f"Книги добавлены в таблицу 'books'.")


def view_books():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    print("\n--- Список книг в базе данных ---")
    for row in rows:
        print(row)

    conn.close()
    print("--------------------------------\n")


if __name__ == "__main__":
    create_table()
    insert_books()
    view_books()

