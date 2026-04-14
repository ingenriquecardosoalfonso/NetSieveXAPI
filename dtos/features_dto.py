class FeaturesDTO:
    def __init__(self, flow):
        self.id                       = flow.id
        self.feature_key              = flow.feature_key
        self.feature_name             = flow.feature_name
        self.description              = flow.description
        self.predicted_class          = flow.predicted_class
        self.description_positive     = flow.description_positive
        self.description_negative     = flow.description_negative
        self.state                    = flow.state
        
    def to_dict(self):
        return {
            "id":                       self.id,
            "feature_key":              self.feature_key,
            "feature_name":             self.feature_name,
            "description":              self.description,
            "predicted_class":          self.predicted_class,
            "description_positive":     self.description_positive,
            "description_negative":     self.description_negative,
            "state":                    self.state,
        }
