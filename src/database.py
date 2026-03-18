import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

# User authentication
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data['username']
    password = data['password']

    conn = create_connection('users.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
        conn.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data['username']
    password = data['password']

    conn = create_connection('users.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
        user = cursor.fetchone()
        if user:
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'message': 'Invalid credentials!'}), 401

if __name__ == '__main__':
    app.run(debug=True)