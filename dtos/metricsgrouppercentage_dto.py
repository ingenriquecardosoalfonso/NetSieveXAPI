class MetricGroupPercentageDTO:
    def __init__(self, metric):
        self.traffic_class             = metric.traffic_class
        self.total_rows                   = metric.total_rows
        self.percentage                   = metric.percentage
        
    def to_dict(self):
        def f(v):
            return float(v) if v is not None else None

        return {
            "traffic_class":            self.traffic_class,
            "total_rows":                  f(self.total_rows),
            "percentage":                  f(self.percentage),
        }
           