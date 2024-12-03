"""Домашнее задание

Задание 1: Создание базы данных и таблицы
Создайте базу данных library.db.
Создайте таблицу books с колонками:
id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
title (TEXT) – название книги
author (TEXT) – автор книги
year (INTEGER) – год издания
Напишите функцию для создания таблицы books, если она еще не существует.

Задание 2: Добавление записей
Напишите функцию add_book, которая добавляет книгу в таблицу books. Функция должна принимать параметры title, author, year.
Добавьте 3 книги с разными значениями для проверки работы функции."""
"""
Задание 3: Поиск книги по названию
Напишите функцию find_book_by_title, которая принимает название книги и возвращает информацию о книге, если она есть в таблице books.
Проверьте функцию, добавив несколько книг и найдя одну из них."""

"""Задание 4: Обновление информации о книге
Напишите функцию update_book_year, которая обновляет год издания книги по ее title.
Проверьте работу функции, изменив год издания для одной из добавленных книг."""

"""Задание 5: Удаление книги по названию
Напишите функцию delete_book_by_title, которая удаляет книгу из базы данных по названию.
Проверьте работу функции, удалив одну из добавленных книг и попытавшись снова найти ее с помощью find_book_by_title.
"""
"""Итоговое задание: Меню для взаимодействия
Напишите программу с меню, чтобы пользователи могли:
Добавлять книгу.
Искать книгу по названию.
Обновлять год издания книги.
Удалять книгу по названию.
Выходить из программы."""


import sqlite3

connect = sqlite3.connect('library.db')
cursor = connect.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
""")

def books():
    title = input("Название книги: ")
    author = input("Автор книги: ")
    year = int(input("Год издания: "))
    cursor.execute("""
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
    """, (title, author, year))
    connect.commit()

def add_book(title, author, year):
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    connect.commit()

def find_book_by_title(title):
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    return cursor.fetchone()

def update_book_year(title, new_year):
    cursor.execute("UPDATE books SET year = ? WHERE title = ?", (new_year, title))
    connect.commit()
    print(f'Год издания книги "{title}" был обновлен на {new_year}')

def delete_book_by_title(title):
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
    connect.commit()
    print(f'Книга с названием "{title}" была удалена')


books()  
add_book("Биринчи мугалим", "Ч.Айтматов", 1962)
# find_book_by_title()
# update_book_year()
# delete_book_by_title()
# def close(self):
#         self.connection.close()
