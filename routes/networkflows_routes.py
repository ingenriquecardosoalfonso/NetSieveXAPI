from flask import Blueprint, request, jsonify
from services.network_flow_service import NetworkFlowService

network_flow_bp = Blueprint('network_flow', __name__)
service = NetworkFlowService()


@network_flow_bp.route('/api/network-flows', methods=['GET'])
def get_all():
    """
    Get all network flows
    ---
    tags:
      - Network Flows
    responses:
      200:
        description: List of all network flows
      500:
        description: Internal server error
    """
    try:
        flows = service.get_all()
        return jsonify(flows), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@network_flow_bp.route('/api/network-flows/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Get a network flow by ID
    ---
    tags:
      - Network Flows
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


@network_flow_bp.route('/api/network-flows', methods=['POST'])
def create():
    """
    Create a new network flow
    ---
    tags:
      - Network Flows
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            proto:
              type: string
              example: TCP
            service:
              type: string
              example: http
            flow_duration:
              type: number
              example: 1.5
            fwd_pkts_tot:
              type: integer
              example: 10
            bwd_pkts_tot:
              type: integer
              example: 5
            flow_pkts_per_sec:
              type: number
              example: 100.0
            down_up_ratio:
              type: number
              example: 0.5
            flow_FIN_flag_count:
              type: integer
              example: 1
            flow_SYN_flag_count:
              type: integer
              example: 1
            flow_RST_flag_count:
              type: integer
              example: 0
            flow_ACK_flag_count:
              type: integer
              example: 3
            fwd_pkts_payload_avg:
              type: number
              example: 512.0
            bwd_pkts_payload_avg:
              type: number
              example: 256.0
            fwd_pkts_payload_tot:
              type: integer
              example: 5120
            fwd_pkts_payload_min:
              type: number
              example: 40.0
            flow_pkts_payload_avg:
              type: number
              example: 400.0
            flow_pkts_payload_std:
              type: number
              example: 50.0
            fwd_iat_avg:
              type: number
              example: 0.01
            bwd_iat_avg:
              type: number
              example: 0.02
            flow_iat_avg:
              type: number
              example: 0.015
            fwd_init_window_size:
              type: integer
              example: 65535
            bwd_init_window_size:
              type: integer
              example: 65535
            fwd_last_window_size:
              type: integer
              example: 512
            payload_bytes_per_second:
              type: number
              example: 3413.33
            fwd_subflow_bytes:
              type: integer
              example: 5120
            fwd_header_size_tot:
              type: integer
              example: 200
            active_avg:
              type: number
              example: 0.5
            active_tot:
              type: number
              example: 1.0
            active_min:
              type: number
              example: 0.1
            id_resp_p:
              type: integer
              example: 80
            bwd_pkts_per_sec:
              type: number
              example: 50.0
            Attack_grouped:
              type: string
              example: Benign
    responses:
      201:
        description: Network flow created successfully
      400:
        description: Incomplete data
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Incomplete data"}), 400

        flow = service.create(data)
        return jsonify(flow), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@network_flow_bp.route('/api/network-flows/<int:id>', methods=['PUT'])
def update(id):
    """
    Update a network flow
    ---
    tags:
      - Network Flows
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID of the network flow to update
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            proto:
              type: string
              example: UDP
            service:
              type: string
              example: dns
            flow_duration:
              type: number
              example: 2.0
            Attack_grouped:
              type: string
              example: DDoS
    responses:
      200:
        description: Network flow updated successfully
      404:
        description: Network flow not found
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Incomplete data"}), 400

        flow = service.update(id, data)
        if not flow:
            return jsonify({"message": "Network flow not found"}), 404

        return jsonify(flow), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@network_flow_bp.route('/api/network-flows/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Delete a network flow
    ---
    tags:
      - Network Flows
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID of the network flow to delete
    responses:
      200:
        description: Network flow deleted successfully
      404:
        description: Network flow not found
      500:
        description: Internal server error
    """
    try:
        deleted = service.delete(id)
        if not deleted:
            return jsonify({"message": "Network flow not found"}), 404
        return jsonify({"message": "Network flow deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
