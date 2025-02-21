from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change for production!
jwt = JWTManager(app)

# In-memory store for demo purposes
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = generate_password_hash(password)
    return jsonify({"msg": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
