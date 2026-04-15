from extensions import db
import uuid

class TrafficClassDistribution(db.Model):
    __tablename__ = 'ViewTrafficClassDistribution'

    label          = db.Column('label',          db.String(100),  primary_key=True)
    count             = db.Column('count',             db.Integer)
    percentage             = db.Column('percentage',             db.Numeric(10,2))

    def __repr__(self):
        return f'<TrafficClassDistribution label={self.label} count={self.count} percentage={self.percentage}>'