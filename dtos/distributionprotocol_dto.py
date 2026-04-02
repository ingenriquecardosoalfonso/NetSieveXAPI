class DistributionProtocolDTO:
    def __init__(self, record):
        self.proto          = record.proto
        self.attack_grouped = record.attack_grouped
        self.count          = record.count

    def to_dict(self):
        return {
            "proto":         self.proto,
            "attackGrouped": self.attack_grouped,
            "count":         self.count,
        }