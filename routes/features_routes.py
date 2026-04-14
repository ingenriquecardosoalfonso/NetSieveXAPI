from flask import Blueprint, request, jsonify
from services.features_service import FeaturesService

features_bp = Blueprint('features', __name__)
service = FeaturesService()


@features_bp.route('/api/features/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Get a feature by ID
    ---
    tags:
      - Features
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID of the network flow
    responses:
      200:
        description: Network flow found
      404:
        description: Network flow not found
      500:
        description: Internal server error
    """
    try:
        flow = service.get_by_id(id)
        if not flow:
            return jsonify({"message": "Network flow not found"}), 404
        return jsonify(flow), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
