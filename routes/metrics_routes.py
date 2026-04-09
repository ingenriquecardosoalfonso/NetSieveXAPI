# routes/metrics.py
from flask import Blueprint
from models.metric import Metric
from models.metricsgroup import MetricGroup
from models.classdistribution import ClassDistribution
from models.distributionprotocol import DistributionProtocol
from models.distributionservice import DistributionService
from dtos.metric_dto import MetricDTO
from dtos.metricsgroup_dto import MetricGroupDTO
from dtos.classdistribution_dto import ClassDistributionDTO
from dtos.distributionprotocol_dto import DistributionProtocolDTO
from dtos.distributionservice_dto import DistributionServiceDTO
from models.metricsgrouppercentage import MetricGroupPercentage
from dtos.metricsgrouppercentage_dto import MetricGroupPercentageDTO
from utils.jwt_decorator import token_required
from utils.route_helpers import query_all

metrics_bp = Blueprint('metrics', __name__, url_prefix='/api/metrics')


@metrics_bp.route('/', methods=['GET'])
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
              totalFlows:
                type: integer
                example: 1500
              maliciousPct:
                type: number
                example: 23.45
      401:
        description: Token inválido o no enviado
      403:
        description: Token no proporcionado
      500:
        description: Error interno del servidor
    """
    return query_all(Metric, MetricDTO)


@metrics_bp.route('/group', methods=['GET'])
@token_required
def get_metrics_group():
    """
    Get metrics grouped by traffic class
    ---
    tags:
      - Metrics
    security:
      - Bearer: []
    responses:
      200:
        description: List of metrics grouped by traffic class
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                example: 550e8400-e29b-41d4-a716-446655440000
              trafficClass:
                type: string
                example: Normal
              sampleCount:
                type: integer
                example: 3200
              avgDuration:
                type: number
                example: 12.5678
              avgPktsPerSec:
                type: number
                example: 45.23
      401:
        description: Token inválido o no enviado
      403:
        description: Token no proporcionado
      500:
        description: Error interno del servidor
    """
    return query_all(MetricGroup, MetricGroupDTO)

@metrics_bp.route('/groupPercentage', methods=['GET'])
@token_required
def get_metrics_group_percentage():
    """
    Get metrics grouped by traffic class with percentage
    ---
    tags:
      - Metrics
    security:
      - Bearer: []
    responses:
      200:
        description: List of metrics grouped by traffic class
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                example: 550e8400-e29b-41d4-a716-446655440000
              trafficClass:
                type: string
                example: Normal
              
              percentage:
                type: number
                example: 35
      401:
        description: Token inválido o no enviado
      403:
        description: Token no proporcionado
      500:
        description: Error interno del servidor
    """
    return query_all(MetricGroupPercentage, MetricGroupPercentageDTO)


@metrics_bp.route('/distributions/class', methods=['GET'])
@token_required
def get_class_distribution():
    """
    Get attack class distribution
    ---
    tags:
      - Metrics
    security:
      - Bearer: []
    responses:
      200:
        description: Distribution of attacks grouped by class
        schema:
          type: array
          items:
            type: object
            properties:
              attackGrouped:
                type: string
                example: DDoS
              count:
                type: integer
                example: 4200
              pct:
                type: number
                example: 35.75
      401:
        description: Token inválido o no enviado
      403:
        description: Token no proporcionado
      500:
        description: Error interno del servidor
    """
    return query_all(ClassDistribution, ClassDistributionDTO)


@metrics_bp.route('/distributions/protocol', methods=['GET'])
@token_required
def get_protocol_distribution():
    """
    Get attack distribution by protocol
    ---
    tags:
      - Metrics
    security:
      - Bearer: []
    responses:
      200:
        description: Distribution of attacks grouped by protocol
        schema:
          type: array
          items:
            type: object
            properties:
              proto:
                type: string
                example: TCP
              attackGrouped:
                type: string
                example: DoS
              count:
                type: integer
                example: 1800
      401:
        description: Token inválido o no enviado
      403:
        description: Token no proporcionado
      500:
        description: Error interno del servidor
    """
    return query_all(DistributionProtocol, DistributionProtocolDTO)


@metrics_bp.route('/distributions/service', methods=['GET'])
@token_required
def get_service_distribution():
    """
    Get attack distribution by service
    ---
    tags:
      - Metrics
    security:
      - Bearer: []
    responses:
      200:
        description: Distribution of attacks grouped by service
        schema:
          type: array
          items:
            type: object
            properties:
              service:
                type: string
                example: http
              attackGrouped:
                type: string
                example: Infiltration
              count:
                type: integer
                example: 950
      401:
        description: Token inválido o no enviado
      403:
        description: Token no proporcionado
      500:
        description: Error interno del servidor
    """
    return query_all(DistributionService, DistributionServiceDTO)