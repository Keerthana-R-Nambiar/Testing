from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

# ❌ Hardcoded secret key (Crypto failure)
SECRET_KEY = "mysecret123"

# ❌ Weak password hashing (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    hashed = hash_password(password)

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{hashed}'"
    cursor.execute(query)

    user = cursor.fetchone()
    if user:
        return "Login successful"
    return "Invalid credentials"

# ❌ Broken Access Control (no authentication check)
@app.route("/admin/delete")
def delete_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id={user_id}")
    conn.commit()
    return "User deleted"

app.run(debug=True)
