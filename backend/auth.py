import jwt
from flask import request, jsonify
from functools import wraps

SECRET_KEY = 'your-secret-key'

def authenticate(username, password):
    return username == "admin" and password == "admin123"

def generate_token(username):
    return jwt.encode({"user": username}, SECRET_KEY, algorithm="HS256")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is missing"}), 403
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data["user"]
        except:
            return jsonify({"error": "Invalid token"}), 403
        return f(current_user, *args, **kwargs)
    return decorated
