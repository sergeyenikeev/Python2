import sqlite3

# Подключение к БД
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Создаем таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()


# C - Create
def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(f"Пользователь {name} добавлен.")


# R - Read
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Список пользователей:")
    for user in users:
        print(user)


def get_user_by_id(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    print("Найден пользователь:", user)


# U - Update
def update_user(user_id, new_name, new_age):
    cursor.execute(
        "UPDATE users SET name = ?, age = ? WHERE id = ?",
        (new_name, new_age, user_id)
    )
    conn.commit()
    print(f"Пользователь с id={user_id} обновлен.")


# D - Deleteгм
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print(f"Пользователь с id={user_id} удален.")


# Пример работы
create_user("Иван", 25)
create_user("Мария", 30)

get_users()
get_user_by_id(1)

update_user(1, "Иван Петров", 26)
get_users()

delete_user(2)
get_users()

# Закрытие соединения
conn.close()