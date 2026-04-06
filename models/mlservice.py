# services/ml_service.py
import joblib
import pandas as pd
from pathlib import Path

from dtos.prediction_dto import PredictionDTO

MODEL_DIR = Path(__file__).parent / "predictive"

# Feature names exactly as the models expect them
FEATURE_COLUMNS = [
    'fwd_subflow_bytes',
    'fwd_pkts_payload.tot',
    'fwd_pkts_payload.avg',
    'flow_pkts_payload.avg',
    'id.resp_p',
    'flow_pkts_payload.std',
    'payload_bytes_per_second',
    'active.avg',
    'active.tot',
    'active.min',
    'flow_pkts_per_sec',
    'flow_iat.avg',
    'fwd_last_window_size',
    'fwd_pkts_payload.min',
    'fwd_header_size_tot',
    'service',
    'proto',
]

class MLService:
    def __init__(self):
        self.models = {
            "decision_tree": joblib.load(MODEL_DIR / "decision_tree.pkl"),
            "knn":           joblib.load(MODEL_DIR / "knn.pkl"),
            "random_forest": joblib.load(MODEL_DIR / "random_forest.pkl"),
        }

    def _flow_to_dataframe(self, flow) -> pd.DataFrame:
        """
        Maps NetworkFlow fields (underscore) to model feature names (dot notation).
        Only the 17 features the models were trained on are included.
        """
        row = {
            'fwd_subflow_bytes':      flow.fwd_subflow_bytes,
            'fwd_pkts_payload.tot':   flow.fwd_pkts_payload_tot,
            'fwd_pkts_payload.avg':   flow.fwd_pkts_payload_avg,
            'flow_pkts_payload.avg':  flow.flow_pkts_payload_avg,
            'id.resp_p':              flow.id_resp_p,
            'flow_pkts_payload.std':  flow.flow_pkts_payload_std,
            'payload_bytes_per_second': flow.payload_bytes_per_second,
            'active.avg':             flow.active_avg,
            'active.tot':             flow.active_tot,
            'active.min':             flow.active_min,
            'flow_pkts_per_sec':      flow.flow_pkts_per_sec,
            'flow_iat.avg':           flow.flow_iat_avg,
            'fwd_last_window_size':   flow.fwd_last_window_size,
            'fwd_pkts_payload.min':   flow.fwd_pkts_payload_min,
            'fwd_header_size_tot':    flow.fwd_header_size_tot,
            'service':                flow.service,
            'proto':                  flow.proto,
        }
        return pd.DataFrame([row], columns=FEATURE_COLUMNS)

    def predict(self, flow, model_name) -> dict:
        df = self._flow_to_dataframe(flow)

        pipeline      = self.models[model_name]
        probabilities = pipeline.predict_proba(df)[0]

        return PredictionDTO(
            model         = model_name,
            prediction    = pipeline.predict(df)[0],
            confidence    = round(float(probabilities.max()), 4),
            probabilities = {cls: round(float(p), 4) for cls, p in zip(pipeline.classes_, probabilities)}
        ).to_dict()
    

       