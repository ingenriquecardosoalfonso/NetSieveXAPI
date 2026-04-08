from flask import Blueprint, request, jsonify
from services.ml_service import MLService

ml_bp   = Blueprint('ml', __name__)
service = MLService()

@ml_bp.route('/api/ml/analyze', methods=['POST'])
def analyze():
    """
    Analyze a network flow and predict if it's benign or malicious using the ML models
    ---
    tags:
      - ML Models
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              example: knn
            proto:
              type: string
              example: tcp
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
    responses:
      200:
        description: Analysis result
      400:
        description: Incomplete data
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Incomplete data"}), 400

        VALID_MODELS = {"random_forest", "decision_tree", "knn"}
        if data.get('model') not in VALID_MODELS:
            return jsonify({"message": f"Invalid or missing model. Choose from: {list(VALID_MODELS)}"}), 400

        result = service.analyze(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    