class ClassDistributionDTO:
    def __init__(self, record):
        self.attack_grouped = record.attack_grouped
        self.count          = record.count
        self.pct            = record.pct

    def to_dict(self):
        return {
            "attackGrouped": self.attack_grouped,
            "count":         self.count,
            "pct":           float(self.pct) if self.pct is not None else None,
        }