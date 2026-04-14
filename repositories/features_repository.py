from extensions import db
from models.features import Feature

class FeaturesRepository:

    def get_by_id(self, id):
        return Feature.query.get(id)
    
    def get_by_key(self, feature_key, prediction):
        return Feature.query.filter_by(feature_key=feature_key, predicted_class=prediction).first()