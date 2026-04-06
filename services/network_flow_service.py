from repositories.network_flow_repository import NetworkFlowRepository
from dtos.networkflows_dto import NetworkFlowDTO

class NetworkFlowService:
    def __init__(self):
        self.repo = NetworkFlowRepository()

    def get_all(self):
        flows = self.repo.get_all()
        return [NetworkFlowDTO(f).to_dict() for f in flows]

    def get_by_id(self, id):
        flow = self.repo.get_by_id(id)
        if not flow:
            return None
        return NetworkFlowDTO(flow).to_dict()

    def create(self, data):
        flow = self.repo.create(data)
        return NetworkFlowDTO(flow).to_dict()

    def update(self, id, data):
        flow = self.repo.update(id, data)
        if not flow:
            return None
        return NetworkFlowDTO(flow).to_dict()

    def delete(self, id):
        return self.repo.delete(id)
    
    def analyze(self, data):
        flow = self.repo.analyze(data)
        return NetworkFlowDTO(flow).to_dict()