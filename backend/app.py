from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# DATABASE INIT
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        status TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# HOME ROUTE
@app.route("/")
def home():
    return "Backend Running 🚀"

# ADD TASK API
@app.route('/add-task', methods=['POST'])
def add_task():
    print(request.headers)  
    print(request.data)     

    data = request.json
    title = data.get('title')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, status) VALUES (?, ?)",
        (title, "pending")
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully"})

# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)