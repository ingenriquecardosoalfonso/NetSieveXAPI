class DistributionServiceDTO:
    def __init__(self, record):
        self.service        = record.service
        self.attack_grouped = record.attack_grouped
        self.count          = record.count

    def to_dict(self):
        return {
            "service":       self.service,
            "attackGrouped": self.attack_grouped,
            "count":         self.count,
        }