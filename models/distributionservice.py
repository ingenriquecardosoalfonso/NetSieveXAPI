# models/distribution_service.py
from extensions import db

class DistributionService(db.Model):
    __tablename__ = 'ViewDistributionService'

    service        = db.Column('service',        db.String(100), primary_key=True)
    attack_grouped = db.Column('Attack_grouped', db.String(100))
    count          = db.Column('count',          db.Integer)

    def __repr__(self):
        return f'<DistributionService service={self.service}>'