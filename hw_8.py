""" Задание: База данных для кинопоиска
Представьте, что вы создаете базу данных для кинотеатра или онлайн-сервиса для учёта фильмов, 
пользователей и их оценок. Требуется реализовать следующие таблицы и функциональность:

1. Movies (фильмы)
id (INTEGER, Primary Key)
title (TEXT) — название фильма.
release_year (INTEGER) — год выпуска.
genre (TEXT) — жанр фильма (например, драма, комедия, триллер).
rating (REAL) — средний рейтинг фильма (от 1 до 10).

3. Users (пользователи)
id (INTEGER, Primary Key)
username (TEXT) — имя пользователя.
email (TEXT, уникальный) — электронная почта пользователя.
registration_date (DATE) — дата регистрации.

3. Reviews (отзывы)
id (INTEGER, Primary Key)
user_id (INTEGER, Foreign Key на Users)
movie_id (INTEGER, Foreign Key на Movies)
review_text (TEXT) — текст отзыва.
rating (REAL) — оценка фильма (от 1 до 10).
review_date (DATE) — дата написания отзыва.


Задания
1. Основная задача: Разработайте и реализуйте SQL-запросы для следующих задач:
Найти все фильмы, выпущенные после 2010 года.
Посчитать среднюю оценку фильма по всем отзывам.
Найти все фильмы, оцененные пользователем с username "JohnDoe".
Найти все фильмы в жанре "драма", которые имеют рейтинг выше 7.
Вывести список пользователей, которые оставили отзыв на фильм с id = 5.
2. Дополнительная задача:
Создать представление, которое будет показывать фильмы, отсортированные по году выпуска и их среднему рейтингу.
3. Проблемное задание: Напишите запрос, который возвращает список пользователей, 
оставивших отзывы на фильмы, у которых рейтинг выше 8.0."""

import sqlite3

class Movies:
    def __init__(self, db_name='cinema.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS films(
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE NOT NULL,
            release_year INT NOT NULL,
            genre TEXT,
            rating REAL
        )
        """)
        self.connection.commit()

class Users:
    def __init__(self, cursor):
        self.cursor = cursor
        self.create_table_users()

    def create_table_users(self):
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            registration_date DATE
        )
        """)
        self.connection.commit()

class Reviews:
    def __init__(self, cursor):
        self.cursor = cursor
        self.create_table_reviews()

    def create_table_reviews(self):
        self.cursor.execute('''   
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            movie_id INTEGER NOT NULL,
            review_text TEXT,
            rating REAL NOT NULL,
            review_date DATE DEFAULT CURRENT_DATE,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (movie_id) REFERENCES films(id)
        )        
        ''')
        self.connection.commit()


class Methods(Movies, Users, Reviews):
    def __init__(self, db_name='cinema.db'):
        Movies.__init__(self, db_name)
        Users.__init__(self, self.cursor)
        Reviews.__init__(self, self.cursor)

    
    def get_year(self):
        self.cursor.execute('''SELECT * FROM films WHERE release_year IN (2011, 2012, 2013)''')
        return self.cursor.fetchall() 
   
    def get_rating(self):
        self.cursor.execute('''SELECT * FROM reviews WHERE rating = 5''')
        return self.cursor.fetchall()

    def get_name(self):
        self.cursor.execute('''SELECT * FROM users WHERE user_name = ?''', ('JohnDoe',)) 
        return self.cursor.fetchone()

    def get_genre(self):
        self.cursor.execute('''SELECT genre FROM films WHERE rating = ?''', (7,))        
        return self.cursor.fetchall()
   
    def get_id(self):
        self.cursor.execute(('''SELECT movie_id FROM films WHERE id = ?''', (8,)))
        return self.cursor.fetchall()
    

# movie = Methods()
# print(movie.get_name())  
# print(movie.get_year())  
# print(movie.get_rating())  
# print(movie.get_genre()) 
# print(movie.get_id())