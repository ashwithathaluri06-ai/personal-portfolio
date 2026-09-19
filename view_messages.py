import sqlite3

connection = sqlite3.connect("portfolio.db")
connection.row_factory = sqlite3.Row

messages = connection.execute(
    "SELECT * FROM messages ORDER BY id DESC"
).fetchall()

for message in messages:
    print("ID:", message["id"])
    print("Name:", message["name"])
    print("Email:", message["email"])
    print("Message:", message["message"])
    print("Date:", message["created_at"])
    print("-" * 40)

connection.close()