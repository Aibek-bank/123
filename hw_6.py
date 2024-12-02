""" Создайте базу назвав таблицу geeks 
c полями id, fullname, number,
также создайте функцию для добавления значения в базу, 
отдельно еще одну функцию для удаления через параметр id """

import sqlite3

connect = sqlite3.connect('geeks.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        number INT DEFAULT NULL) """)

def register():
    id = int(input("Введите id: "))
    full_name = input("Введите имя: ")
    number = int(input("Введите номер: "))

    cursor.execute(f""" INSERT INTO users
                   (id, full_name, number)
                   VALUES ({id}, '{full_name}', {number})""")
    connect.commit()
register()

def delete():
    cursor.execute("SELECT * FROM users ")
    students = cursor.fetchone()
    print(students)

delete()