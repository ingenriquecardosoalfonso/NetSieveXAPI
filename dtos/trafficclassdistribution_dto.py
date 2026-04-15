class TrafficClassDistributionDTO:
    def __init__(self, metric):
        self.label             = metric.label
        self.count                   = metric.count
        self.percentage                   = metric.percentage
        
    def to_dict(self):
        def f(v):
            return float(v) if v is not None else None

        return {
            "label":            self.label,
            "count":                  f(self.count),
            "percentage":                  f(self.percentage),
        }