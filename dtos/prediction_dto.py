# dtos/prediction_dto.py
from dataclasses import dataclass, asdict

@dataclass
class PredictionDTO:
    model:         str
    prediction:    str
    confidence:    float
    probabilities: dict

    def to_dict(self):
        return asdict(self)