from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "portfolio.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            technologies TEXT NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    connection = get_db_connection()

    projects = connection.execute(
        "SELECT * FROM projects"
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        projects=projects
    )


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO messages (name, email, message)
        VALUES (?, ?, ?)
        """,
        (name, email, message)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)