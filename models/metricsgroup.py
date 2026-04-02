from extensions import db
import uuid

class MetricGroup(db.Model):
    __tablename__ = 'ViewMetricsGroup'

    id                       = db.Column('id',                       db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    sample_count             = db.Column('sample_count',             db.Integer)
    avg_duration             = db.Column('avg_duration',             db.Numeric(10,4))
    avg_pkts_per_sec         = db.Column('avg_pkts_per_sec',         db.Numeric(10,2))
    traffic_class            = db.Column('traffic_class',            db.String(6),  nullable=False)
    avg_syn                  = db.Column('avg_syn',                  db.Numeric(10,2))
    avg_ack                  = db.Column('avg_ack',                  db.Numeric(10,2))
    avg_rst                  = db.Column('avg_rst',                  db.Numeric(10,2))
    avg_fin                  = db.Column('avg_fin',                  db.Numeric(10,2))
    avg_down_up_ratio        = db.Column('avg_down_up_ratio',        db.Numeric(10,4))
    avg_payload_bytes_per_sec= db.Column('avg_payload_bytes_per_sec',db.Numeric(10,2))
    avg_fwd_subflow_bytes    = db.Column('avg_fwd_subflow_bytes',    db.Numeric(10,2))
    avg_payload_std          = db.Column('avg_payload_std',          db.Numeric(10,2))
    avg_pkts                 = db.Column('avg_pkts',                 db.Numeric(10,2))
    avg_payload_per_pkt      = db.Column('avg_payload_per_pkt',      db.Numeric(10,2))
    avg_payload_bytes_sec    = db.Column('avg_payload_bytes_sec',    db.Numeric(10,2))
    avg_fwd_header_size      = db.Column('avg_fwd_header_size',      db.Numeric(10,0))
    avg_active_time          = db.Column('avg_active_time',          db.Numeric(10,4))

    def __repr__(self):
        return f'<MetricGroup id={self.id} traffic_class={self.traffic_class}>'