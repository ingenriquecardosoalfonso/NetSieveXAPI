class MetricDTO:
    def __init__(self, metric):
        self.total_flows        = metric.total_flows
        self.malicious_pct      = metric.malicious_pct
        self.avg_pkts_per_sec   = metric.avg_pkts_per_sec
        self.avg_duration_sec   = metric.avg_duration_sec
        self.flow_pkts_per_sec              = metric.flow_pkts_per_sec
        self.avg_bytes_per_sec  = metric.avg_bytes_per_sec
        self.threat_pct         = metric.threat_pct
        self.avg_duration       = metric.avg_duration
        self.min_pkts           = metric.min_pkts
        self.max_pkts           = metric.max_pkts
        self.min_dur            = metric.min_dur
        self.max_dur            = metric.max_dur
        self.min_pay            = metric.min_pay
        self.max_pay            = metric.max_pay
        self.min_fwd            = metric.min_fwd
        self.max_fwd            = metric.max_fwd
        self.min_bwd            = metric.min_bwd
        self.max_bwd            = metric.max_bwd
        self.min_syn            = metric.min_syn
        self.max_syn            = metric.max_syn
        self.min_ack            = metric.min_ack
        self.max_ack            = metric.max_ack
        self.min_rst            = metric.min_rst
        self.max_rst            = metric.max_rst
        self.min_fin            = metric.min_fin
        self.max_fin            = metric.max_fin
        self.min_fwd_avg        = metric.min_fwd_avg
        self.max_fwd_avg        = metric.max_fwd_avg
        self.min_fwd_min        = metric.min_fwd_min
        self.max_fwd_min        = metric.max_fwd_min
        self.min_fwd_iat        = metric.min_fwd_iat
        self.max_fwd_iat        = metric.max_fwd_iat
        self.min_bwd_iat        = metric.min_bwd_iat
        self.max_bwd_iat        = metric.max_bwd_iat
        self.min_fwd_win        = metric.min_fwd_win
        self.max_fwd_win        = metric.max_fwd_win
        self.min_bwd_win        = metric.min_bwd_win
        self.max_bwd_win        = metric.max_bwd_win
        self.min_fwd_lwin       = metric.min_fwd_lwin
        self.max_fwd_lwin       = metric.max_fwd_lwin

    def to_dict(self):
        return {
            "totalFlows":       self.total_flows,
            "maliciousPct":     float(self.malicious_pct)     if self.malicious_pct     is not None else None,
            "avgPktsPerSec":    float(self.avg_pkts_per_sec)  if self.avg_pkts_per_sec  is not None else None,
            "avgDurationSec":   float(self.avg_duration_sec)  if self.avg_duration_sec  is not None else None,
            "flow_pkts_per_sec":            float(self.flow_pkts_per_sec)             if self.flow_pkts_per_sec             is not None else None,
            "avgBytesPerSec":   float(self.avg_bytes_per_sec) if self.avg_bytes_per_sec is not None else None,
            "threatPct":        float(self.threat_pct)        if self.threat_pct        is not None else None,
            "avgDuration":      float(self.avg_duration)      if self.avg_duration      is not None else None,
            "minPkts":          self.min_pkts,
            "maxPkts":          self.max_pkts,
            "minDur":           self.min_dur,
            "maxDur":           self.max_dur,
            "minPay":           self.min_pay,
            "maxPay":           self.max_pay,
            "minFwd":           self.min_fwd,
            "maxFwd":           self.max_fwd,
            "minBwd":           self.min_bwd,
            "maxBwd":           self.max_bwd,
            "minSyn":           self.min_syn,
            "maxSyn":           self.max_syn,
            "minAck":           self.min_ack,
            "maxAck":           self.max_ack,
            "minRst":           self.min_rst,
            "maxRst":           self.max_rst,
            "minFin":           self.min_fin,
            "maxFin":           self.max_fin,
            "minFwdAvg":        self.min_fwd_avg,
            "maxFwdAvg":        self.max_fwd_avg,
            "minFwdMin":        self.min_fwd_min,
            "maxFwdMin":        self.max_fwd_min,
            "minFwdIat":        self.min_fwd_iat,
            "maxFwdIat":        self.max_fwd_iat,
            "minBwdIat":        self.min_bwd_iat,
            "maxBwdIat":        self.max_bwd_iat,
            "minFwdWin":        self.min_fwd_win,
            "maxFwdWin":        self.max_fwd_win,
            "minBwdWin":        self.min_bwd_win,
            "maxBwdWin":        self.max_bwd_win,
            "minFwdLwin":       self.min_fwd_lwin,
            "maxFwdLwin":       self.max_fwd_lwin,
        }