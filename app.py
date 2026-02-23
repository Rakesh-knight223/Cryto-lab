from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "Alice", "email": "alice@test.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@test.com"},
    3: {"id": 3, "name": "Charlie", "email": "charlie@test.com"}
}

@app.route("/api/users/<int:user_id>")
def get_user(user_id):
    # ❌ BOLA vulnerability: no authorization check
    return jsonify(users.get(user_id, {"error": "User not found"}))

@app.route("/")
def home():
    return "BOLA Lab Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
