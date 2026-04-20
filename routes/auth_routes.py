from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
service = AuthService()


@auth_bp.route('/auth/register', methods=['POST'])
def register():
    """
    Create user
    ---
    tags:
      - Auth
    """
    try:
        data = request.get_json(silent=True, force=True)

        if not data or not data.get("name") or not data.get("email") or not data.get("password"):
            return jsonify({"mensaje": "Datos incompletos"}), 400

        service.register(
            data['name'],
            data['email'],
            data['password']
        )

        return jsonify({"mensaje": "User created successfully"}), 200

    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    """
    Login of user
    ---
    tags:
      - Auth
    """
    try:
        data = request.get_json(silent=True, force=True)

        if not data or not data.get("email") or not data.get("password"):
            return jsonify({"mensaje": "Datos incompletos"}), 400

        token = service.login(data['email'], data['password'])

        if not token:
            return jsonify({"mensaje": "Credenciales inválidas"}), 401

        return jsonify({"token": token}), 200

    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500