from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
service = AuthService()


@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    """
    Registrar usuario
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nombre
            - email
            - password
          properties:
            nombre:
              type: string
              example: Juan
            email:
              type: string
              example: juan@test.com
            password:
              type: string
              example: 123456
    responses:
      200:
        description: Usuario creado correctamente
      400:
        description: Error en los datos
    """
    try:
        data = request.get_json()

        if not data or not data.get("nombre") or not data.get("email") or not data.get("password"):
            return jsonify({"mensaje": "Datos incompletos"}), 400

        service.register(
            data['nombre'],
            data['email'],
            data['password']
        )

        return jsonify({"mensaje": "Usuario creado correctamente"}), 200

    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500


@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """
    Login de usuario
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: juan@test.com
            password:
              type: string
              example: 123456
    responses:
      200:
        description: Retorna un token JWT
        schema:
          type: object
          properties:
            token:
              type: string
      401:
        description: Credenciales inválidas
    """
    try:
        data = request.get_json()

        if not data or not data.get("email") or not data.get("password"):
            return jsonify({"mensaje": "Datos incompletos"}), 400

        token = service.login(data['email'], data['password'])

        if not token:
            return jsonify({"mensaje": "Credenciales inválidas"}), 401

        return jsonify({"token": token}), 200

    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500