from extensions import db

class NetworkFlow(db.Model):
    __tablename__ = 'network_flows'

    id                      = db.Column(db.Integer, primary_key=True)
    proto                   = db.Column(db.String(50),  nullable=True)
    service                 = db.Column(db.String(100), nullable=True)
    flow_duration           = db.Column(db.Float,       nullable=True)
    fwd_pkts_tot            = db.Column(db.BigInteger,  nullable=True)
    bwd_pkts_tot            = db.Column(db.BigInteger,  nullable=True)
    flow_pkts_per_sec       = db.Column(db.Float,       nullable=True)
    down_up_ratio           = db.Column(db.Float,       nullable=True)
    flow_FIN_flag_count     = db.Column(db.Integer,     nullable=True)
    flow_SYN_flag_count     = db.Column(db.Integer,     nullable=True)
    flow_RST_flag_count     = db.Column(db.Integer,     nullable=True)
    flow_ACK_flag_count     = db.Column(db.Integer,     nullable=True)
    fwd_pkts_payload_avg    = db.Column(db.Float,       nullable=True)
    bwd_pkts_payload_avg    = db.Column(db.Float,       nullable=True)
    fwd_pkts_payload_tot    = db.Column(db.BigInteger,  nullable=True)
    fwd_pkts_payload_min    = db.Column(db.Float,       nullable=True)
    flow_pkts_payload_avg   = db.Column(db.Float,       nullable=True)
    flow_pkts_payload_std   = db.Column(db.Float,       nullable=True)
    fwd_iat_avg             = db.Column(db.Float,       nullable=True)
    bwd_iat_avg             = db.Column(db.Float,       nullable=True)
    flow_iat_avg            = db.Column(db.Float,       nullable=True)
    fwd_init_window_size    = db.Column(db.Integer,     nullable=True)
    bwd_init_window_size    = db.Column(db.Integer,     nullable=True)
    fwd_last_window_size    = db.Column(db.Integer,     nullable=True)
    payload_bytes_per_second= db.Column(db.Float,       nullable=True)
    fwd_subflow_bytes       = db.Column(db.BigInteger,  nullable=True)
    fwd_header_size_tot     = db.Column(db.BigInteger,  nullable=True)
    active_avg              = db.Column(db.Float,       nullable=True)
    active_tot              = db.Column(db.Float,       nullable=True)
    active_min              = db.Column(db.Float,       nullable=True)
    id_resp_p               = db.Column(db.Integer,     nullable=True)
    bwd_pkts_per_sec        = db.Column(db.Float,       nullable=True)
    Attack_grouped          = db.Column(db.String(100), nullable=True)

    def __init__(self, proto=None, service=None, flow_duration=None,
                 fwd_pkts_tot=None, bwd_pkts_tot=None, flow_pkts_per_sec=None,
                 down_up_ratio=None, flow_FIN_flag_count=None, flow_SYN_flag_count=None,
                 flow_RST_flag_count=None, flow_ACK_flag_count=None,
                 fwd_pkts_payload_avg=None, bwd_pkts_payload_avg=None,
                 fwd_pkts_payload_tot=None, fwd_pkts_payload_min=None,
                 flow_pkts_payload_avg=None, flow_pkts_payload_std=None,
                 fwd_iat_avg=None, bwd_iat_avg=None, flow_iat_avg=None,
                 fwd_init_window_size=None, bwd_init_window_size=None,
                 fwd_last_window_size=None, payload_bytes_per_second=None,
                 fwd_subflow_bytes=None, fwd_header_size_tot=None,
                 active_avg=None, active_tot=None, active_min=None,
                 id_resp_p=None, bwd_pkts_per_sec=None, Attack_grouped=None):

        self.proto                  = proto
        self.service                = service
        self.flow_duration          = flow_duration
        self.fwd_pkts_tot           = fwd_pkts_tot
        self.bwd_pkts_tot           = bwd_pkts_tot
        self.flow_pkts_per_sec      = flow_pkts_per_sec
        self.down_up_ratio          = down_up_ratio
        self.flow_FIN_flag_count    = flow_FIN_flag_count
        self.flow_SYN_flag_count    = flow_SYN_flag_count
        self.flow_RST_flag_count    = flow_RST_flag_count
        self.flow_ACK_flag_count    = flow_ACK_flag_count
        self.fwd_pkts_payload_avg   = fwd_pkts_payload_avg
        self.bwd_pkts_payload_avg   = bwd_pkts_payload_avg
        self.fwd_pkts_payload_tot   = fwd_pkts_payload_tot
        self.fwd_pkts_payload_min   = fwd_pkts_payload_min
        self.flow_pkts_payload_avg  = flow_pkts_payload_avg
        self.flow_pkts_payload_std  = flow_pkts_payload_std
        self.fwd_iat_avg            = fwd_iat_avg
        self.bwd_iat_avg            = bwd_iat_avg
        self.flow_iat_avg           = flow_iat_avg
        self.fwd_init_window_size   = fwd_init_window_size
        self.bwd_init_window_size   = bwd_init_window_size
        self.fwd_last_window_size   = fwd_last_window_size
        self.payload_bytes_per_second = payload_bytes_per_second
        self.fwd_subflow_bytes      = fwd_subflow_bytes
        self.fwd_header_size_tot    = fwd_header_size_tot
        self.active_avg             = active_avg
        self.active_tot             = active_tot
        self.active_min             = active_min
        self.id_resp_p              = id_resp_p
        self.bwd_pkts_per_sec       = bwd_pkts_per_sec
        self.Attack_grouped         = Attack_grouped