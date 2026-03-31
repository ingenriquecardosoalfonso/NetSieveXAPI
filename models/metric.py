from extensions import db

class Metric(db.Model):
    __tablename__ = 'ViewMetrics'
    
    totalFlows = db.Column(db.Integer, primary_key=True, nullable=False)

    def __repr__(self):
        return f'<Metric totalFlows={self.totalFlows}>'