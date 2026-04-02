class MetricGroupDTO:
    def __init__(self, metric):
        self.id                        = str(metric.id)
        self.sample_count              = metric.sample_count
        self.avg_duration              = metric.avg_duration
        self.avg_pkts_per_sec          = metric.avg_pkts_per_sec
        self.traffic_class             = metric.traffic_class
        self.avg_syn                   = metric.avg_syn
        self.avg_ack                   = metric.avg_ack
        self.avg_rst                   = metric.avg_rst
        self.avg_fin                   = metric.avg_fin
        self.avg_down_up_ratio         = metric.avg_down_up_ratio
        self.avg_payload_bytes_per_sec = metric.avg_payload_bytes_per_sec
        self.avg_fwd_subflow_bytes     = metric.avg_fwd_subflow_bytes
        self.avg_payload_std           = metric.avg_payload_std
        self.avg_pkts                  = metric.avg_pkts
        self.avg_payload_per_pkt       = metric.avg_payload_per_pkt
        self.avg_payload_bytes_sec     = metric.avg_payload_bytes_sec
        self.avg_fwd_header_size       = metric.avg_fwd_header_size
        self.avg_active_time           = metric.avg_active_time

    def to_dict(self):
        def f(v):
            return float(v) if v is not None else None

        return {
            "id":                      self.id,
            "sampleCount":             self.sample_count,
            "avgDuration":             f(self.avg_duration),
            "avgPktsPerSec":           f(self.avg_pkts_per_sec),
            "trafficClass":            self.traffic_class,
            "avgSyn":                  f(self.avg_syn),
            "avgAck":                  f(self.avg_ack),
            "avgRst":                  f(self.avg_rst),
            "avgFin":                  f(self.avg_fin),
            "avgDownUpRatio":          f(self.avg_down_up_ratio),
            "avgPayloadBytesPerSec":   f(self.avg_payload_bytes_per_sec),
            "avgFwdSubflowBytes":      f(self.avg_fwd_subflow_bytes),
            "avgPayloadStd":           f(self.avg_payload_std),
            "avgPkts":                 f(self.avg_pkts),
            "avgPayloadPerPkt":        f(self.avg_payload_per_pkt),
            "avgPayloadBytesSec":      f(self.avg_payload_bytes_sec),
            "avgFwdHeaderSize":        f(self.avg_fwd_header_size),
            "avgActiveTime":           f(self.avg_active_time),
        }