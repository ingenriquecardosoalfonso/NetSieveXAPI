from extensions import db

class DistributionProtocol(db.Model):
    __tablename__ = 'ViewDistributionProtocol'

    proto          = db.Column('proto',          db.String(50),  primary_key=True)
    attack_grouped = db.Column('Attack_grouped', db.String(100))
    count          = db.Column('count',          db.Integer)

    def __repr__(self):
        return f'<DistributionProtocol proto={self.proto}>'