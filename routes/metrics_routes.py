from flask import Blueprint, jsonify
from models.metric import Metric
from dtos.metric_dto import MetricDTO
from utils.jwt_decorator import token_required

metrics_bp = Blueprint('metrics', __name__)

@metrics_bp.route('/api/metrics', methods=['GET'])
@token_required
def get_metrics():
    """
    Get list of metrics
    ---
    tags:
      - Metrics
    security:
      - Bearer: []
    responses:
      200:
        description: List of metrics
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
        metrics = Metric.query.all()

        if not metrics:
            return jsonify([]), 200

        resultado = [MetricDTO(m).to_dict() for m in metrics]
        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500