# services/ml_service.py
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
import shap

from dtos.prediction_dto import PredictionDTO
from repositories.network_flow_repository import NetworkFlowRepository

MODEL_DIR = Path(__file__).parent.parent / "predictive" / "models"
DATA_PATH = Path(__file__).parent.parent / "predictive" / "data" / "background_sample.npy"

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

RISK_LEVELS = {
    "Normal":         "LOW",
    "NMAP":           "MEDIUM",
    "ARP_poisioning": "HIGH",
    "DOS_SYN_Hping":  "CRITICAL",
}

class MLService:
    def __init__(self):
        self.repo = NetworkFlowRepository()
        self.models = {
            "decision_tree": joblib.load(MODEL_DIR / "decision_tree.pkl"),
            "knn":           joblib.load(MODEL_DIR / "knn.pkl"),
            "random_forest": joblib.load(MODEL_DIR / "random_forest.pkl"),
        }

        self.explainers = {
            "decision_tree": shap.TreeExplainer(
                self.models["decision_tree"].named_steps["model"]
            ),
            "random_forest": shap.TreeExplainer(
                self.models["random_forest"].named_steps["model"]
            ),
            "knn": None,
        }
        self._init_knn_explainer() 

    def _init_knn_explainer(self):
        try:
            background = np.load(DATA_PATH)
            self.explainers["knn"] = shap.KernelExplainer(
                self.models["knn"].named_steps["model"].predict_proba,
                background
            )
        except Exception as e:
            print(f"KNN explainer init failed: {e}")
            self.explainers["knn"] = None

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
    
    def _get_risk_level(self, prediction: str, confidence: float) -> str:
        base_level = RISK_LEVELS.get(prediction, "UNKNOWN")
        if confidence < 0.6 and base_level != "LOW":
            return "MEDIUM"
        return base_level

    def _get_shap_features(self, model_name: str, pipeline, df: pd.DataFrame, prediction: str) -> list:
        try:
            df_transformed = pipeline.named_steps["preprocess"].transform(df)
            
            # Convert sparse to dense if needed
            if hasattr(df_transformed, "toarray"):
                df_transformed = df_transformed.toarray()
                
            feature_names  = pipeline.named_steps["preprocess"].get_feature_names_out()
            prediction_idx = pipeline.classes_.tolist().index(prediction)

            if model_name in ("decision_tree", "random_forest"):
                explainer   = self.explainers[model_name]
                shap_values = explainer.shap_values(df_transformed)
                
                if isinstance(shap_values, list):
                    # Multi-class list: [n_classes][n_samples, n_features]
                    values = shap_values[prediction_idx][0]
                elif shap_values.ndim == 3:
                    # 3D array: [n_samples, n_features, n_classes]
                    values = shap_values[0, :, prediction_idx]
                else:
                    # 2D fallback
                    values = shap_values[0]

            elif model_name == "knn":
                if self.explainers["knn"] is None:
                    return []
                shap_values = self.explainers["knn"].shap_values(
                    df_transformed,
                    nsamples=50,
                    l1_reg="num_features(5)"
                )
                if isinstance(shap_values, list):
                    values = shap_values[prediction_idx][0]
                elif shap_values.ndim == 3:
                    values = shap_values[0, :, prediction_idx]
                else:
                    values = shap_values[0]

            importance = sorted(
                zip(feature_names, values),
                key=lambda x: abs(x[1]),
                reverse=True
            )[:5]

            return [
                {"feature": name, "shap_value": round(float(val), 4)}
                for name, val in importance
            ]

        except Exception as e:
            print(f"SHAP explanation failed for {model_name}: {e}")
            return []

    def predict(self, flow, model_name) -> dict:
        df            = self._flow_to_dataframe(flow)
        pipeline      = self.models[model_name]
        probabilities = pipeline.predict_proba(df)[0]
        prediction    = pipeline.predict(df)[0]
        confidence    = round(float(probabilities.max()), 4)

        return PredictionDTO(
            model         = model_name,
            prediction    = prediction,
            confidence    = confidence,
            probabilities = {
                cls: round(float(p), 4)
                for cls, p in zip(pipeline.classes_, probabilities)
            },
            risk_level    = self._get_risk_level(prediction, confidence),
            shap_features = self._get_shap_features(model_name, pipeline, df, prediction)
        ).to_dict()
    
    def analyze(self, data):
        selected_model = data.get('model')

        # 1. Build the flow object
        flow = self.repo.build_flow(data)

        # 2. Run prediction (business logic - belongs in service)
        results = self.predict(flow, model_name=selected_model)

        # 3. Save to DB
        self.repo.save_flow(flow, results['prediction'])

        return results
       