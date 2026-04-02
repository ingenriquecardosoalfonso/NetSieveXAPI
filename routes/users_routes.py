from flask import Blueprint, jsonify
from models.user import User
from dtos.user_dto import UserDTO
from utils.jwt_decorator import token_required

users_bp = Blueprint('users', __name__)

@users_bp.route('/api/users', methods=['GET'])
@token_required
def get_users():
    """
    Get list of users
    ---
    tags:
      - Users
    security:
      - Bearer: []
    responses:
      200:
        description: List of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: Juan
              email:
                type: string
                example: juan@test.com
      401:
        description: Token inválido o no enviado
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: Token inválido o expirado
      403:
        description: Token no proporcionado
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: Token requerido
      500:
        description: Error interno del servidor
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: Error interno del servidor
    """
    try:
        users = User.query.all()

        if not users:
            return jsonify([]), 200

        resultado = [UserDTO(u).to_dict() for u in users]

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500