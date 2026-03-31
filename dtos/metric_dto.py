class MetricDTO:
    def __init__(self, metric):
        self.totalFlows = metric.totalFlows
    def to_dict(self):
        return {
            "totalFlows": self.totalFlows
        }
        