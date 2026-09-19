import sqlite3

DATABASE = "portfolio.db"

connection = sqlite3.connect(DATABASE)

projects = [
    (
        "AI Career & Skill Recommendation System",
        "A Flask-based web application that recommends suitable career paths and identifies matching skills based on user interests and skills.",
        "Python, Flask, HTML, CSS"
    ),
    (
        "Food Image AI Agent",
        "An AI-based project involving food data processing, image search, image downloading and automated image quality processing.",
        "Python, OpenCV, Pillow"
    ),
    (
        "Data Analytics Projects",
        "Data analytics work involving data cleaning, dashboards, customer segmentation and predictive analytics.",
        "Excel, Power BI, Python"
    )
]

for project in projects:
    connection.execute(
        """
        INSERT INTO projects (title, description, technologies)
        VALUES (?, ?, ?)
        """,
        project
    )

connection.commit()
connection.close()

print("Projects added successfully!")