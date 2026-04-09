from extensions import db
import uuid

class MetricGroupPercentage(db.Model):
    __tablename__ = 'ViewMetricsGroupPercentage'

    traffic_class          = db.Column('traffic_class',          db.String(100),  primary_key=True)
    total_rows             = db.Column('total_rows',             db.Integer)
    percentage             = db.Column('percentage',             db.Numeric(10,4))

    def __repr__(self):
        return f'<MetricGroup traffic_class={self.traffic_class} total_rows={self.total_rows} percentage={self.percentage}>'