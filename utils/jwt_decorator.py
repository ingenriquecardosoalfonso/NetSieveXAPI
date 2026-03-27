import jwt
from flask import request, jsonify, g
from functools import wraps
from config import Config  # ← importa Config directamente

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
            return jsonify({"mensaje": "Token no proporcionado"}), 403

        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            g.usuario_id = payload.get('user_id')  # ← coincide con lo que guarda auth_service
        except jwt.ExpiredSignatureError:
            return jsonify({"mensaje": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"mensaje": "Token inválido"}), 401

        return f(*args, **kwargs)

    return decorated