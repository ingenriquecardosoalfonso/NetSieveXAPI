from flask import Blueprint, jsonify
from models.usuario import Usuario
from dtos.usuario_dto import UsuarioDTO
from utils.jwt_decorator import token_required

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/api/usuarios', methods=['GET'])
@token_required
def obtener_usuarios():
    """
    Obtener lista de usuarios
    ---
    tags:
      - Usuarios
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de usuarios
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              nombre:
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
        usuarios = Usuario.query.all()

        if not usuarios:
            return jsonify([]), 200

        resultado = [UsuarioDTO(u).to_dict() for u in usuarios]

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500