import jwt
from flask import request, jsonify, g
from functools import wraps
from config import Config  

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]

        if not token:
            return jsonify({"message": "Token not provided"}), 403

        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            g.user_id = payload.get('user_id')  
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated