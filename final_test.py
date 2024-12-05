import sqlite3

class DatabaseManager:
    def __init__(self, db_name = 'users.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def close(self):
        self.connection.close()

    def find_user_by_name(self, name):
        user_data = self.db.get_user(name)
        if user_data:
            return User(name=user_data[1], email=user_data[2], age=user_data[3])
        else:
            print("Пользователь не найден")

class User:
    def create_table(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (30) NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
            )
        """)
        
        self.connection.commit()

    def add_user(self, user):
        self.cursor.execute(" INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (user.name, user.email, user.age))

        self.connection.commit()

    def get_user(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
class Admin(User):
    def __init__(self, db_name='users.db'):
        self.db = DatabaseManager()

    def add_user(self, user):
        if self.find_user_by_email(user.email):
            print('Пользователь с таким email уже существует')
            return
        self.db.add_user(user)
        print('Пользователь успешно добавлен')

    def show(self, user):
        if self.find_user_by_email(user.email):
            print('Пользователь с таким email есть в списке')
            return
        else:
            print("Пользователь не найден")

class Customer(User):
    def __init__(self, db_name='users.db'):
        self.db = DatabaseManager()

    def show(self, user):
        if self.find_user_by_email(user.email):
            print('Пользователь с таким email есть в списке')
            return
        else:
            print("Пользователь не найден")


add_user()




