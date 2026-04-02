# models/class_distribution.py
from extensions import db

class ClassDistribution(db.Model):
    __tablename__ = 'ViewClassDistribution'

    attack_grouped = db.Column('attack_grouped', db.String(100), primary_key=True)
    count          = db.Column('count',          db.Integer)
    pct            = db.Column('pct',            db.Numeric(10, 2))

    def __repr__(self):
        return f'<ClassDistribution attack_grouped={self.attack_grouped}>'