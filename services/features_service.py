from repositories.features_repository import FeaturesRepository
from dtos.features_dto import FeaturesDTO

class FeaturesService:
    def __init__(self):
        self.repo = FeaturesRepository()

    def get_by_id(self, id):
        flow = self.repo.get_by_id(id)
        if not flow:
            return None
        return FeaturesDTO(flow).to_dict()
    
    def get_by_key(self, feature_key, prediction):
        feature = self.repo.get_by_key(feature_key, prediction)
        if not feature:
            return None
        return FeaturesDTO(feature).to_dict()
    