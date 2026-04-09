# dtos/prediction_dto.py
from dataclasses import dataclass, asdict, field

@dataclass
class PredictionDTO:
    model:         str
    prediction:    str
    confidence:    float
    probabilities: dict
    risk_level:    str  = "UNKNOWN"
    shap_features: list = field(default_factory=list)

    def to_dict(self):
        return asdict(self)