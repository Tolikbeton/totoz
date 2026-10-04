import hashlib
import sqlite3

connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        login TEXT,
        password TEXT,
        email TEXT
    )
"""
)
connection.commit()

print("Нужно ввести данные для 3 пользователей:")

for i in range(3):
  print(f"\n--- Пользователь {i + 1} ---")
  login = input("Login    : ")
  passw = input("Password : ")
  email = input("Email    : ")
  h = hashlib.sha256()
  h.update(passw.encode("utf-8"))
  h_pass = h.hexdigest()

  cur.execute(
      f"INSERT INTO users (login, password, email) VALUES ('{login}',"
      f" '{h_pass}', '{email}')"
  )
  connection.commit()

connection.close()
print("\nГотово! Все 3 пользователя успешно записаны в базу.")

