class NetworkFlowDTO:
    def __init__(self, flow):
        self.id                       = flow.id
        self.proto                    = flow.proto
        self.service                  = flow.service
        self.flow_duration            = flow.flow_duration
        self.fwd_pkts_tot             = flow.fwd_pkts_tot
        self.bwd_pkts_tot             = flow.bwd_pkts_tot
        self.flow_pkts_per_sec        = flow.flow_pkts_per_sec
        self.down_up_ratio            = flow.down_up_ratio
        self.flow_FIN_flag_count      = flow.flow_FIN_flag_count
        self.flow_SYN_flag_count      = flow.flow_SYN_flag_count
        self.flow_RST_flag_count      = flow.flow_RST_flag_count
        self.flow_ACK_flag_count      = flow.flow_ACK_flag_count
        self.fwd_pkts_payload_avg     = flow.fwd_pkts_payload_avg
        self.bwd_pkts_payload_avg     = flow.bwd_pkts_payload_avg
        self.fwd_pkts_payload_tot     = flow.fwd_pkts_payload_tot
        self.fwd_pkts_payload_min     = flow.fwd_pkts_payload_min
        self.flow_pkts_payload_avg    = flow.flow_pkts_payload_avg
        self.flow_pkts_payload_std    = flow.flow_pkts_payload_std
        self.fwd_iat_avg              = flow.fwd_iat_avg
        self.bwd_iat_avg              = flow.bwd_iat_avg
        self.flow_iat_avg             = flow.flow_iat_avg
        self.fwd_init_window_size     = flow.fwd_init_window_size
        self.bwd_init_window_size     = flow.bwd_init_window_size
        self.fwd_last_window_size     = flow.fwd_last_window_size
        self.payload_bytes_per_second = flow.payload_bytes_per_second
        self.fwd_subflow_bytes        = flow.fwd_subflow_bytes
        self.fwd_header_size_tot      = flow.fwd_header_size_tot
        self.active_avg               = flow.active_avg
        self.active_tot               = flow.active_tot
        self.active_min               = flow.active_min
        self.id_resp_p                = flow.id_resp_p
        self.bwd_pkts_per_sec         = flow.bwd_pkts_per_sec
        self.Attack_grouped           = flow.Attack_grouped

    def to_dict(self):
        return {
            "id":                       self.id,
            "proto":                    self.proto,
            "service":                  self.service,
            "flow_duration":            self.flow_duration,
            "fwd_pkts_tot":             self.fwd_pkts_tot,
            "bwd_pkts_tot":             self.bwd_pkts_tot,
            "flow_pkts_per_sec":        self.flow_pkts_per_sec,
            "down_up_ratio":            self.down_up_ratio,
            "flow_FIN_flag_count":      self.flow_FIN_flag_count,
            "flow_SYN_flag_count":      self.flow_SYN_flag_count,
            "flow_RST_flag_count":      self.flow_RST_flag_count,
            "flow_ACK_flag_count":      self.flow_ACK_flag_count,
            "fwd_pkts_payload_avg":     self.fwd_pkts_payload_avg,
            "bwd_pkts_payload_avg":     self.bwd_pkts_payload_avg,
            "fwd_pkts_payload_tot":     self.fwd_pkts_payload_tot,
            "fwd_pkts_payload_min":     self.fwd_pkts_payload_min,
            "flow_pkts_payload_avg":    self.flow_pkts_payload_avg,
            "flow_pkts_payload_std":    self.flow_pkts_payload_std,
            "fwd_iat_avg":              self.fwd_iat_avg,
            "bwd_iat_avg":              self.bwd_iat_avg,
            "flow_iat_avg":             self.flow_iat_avg,
            "fwd_init_window_size":     self.fwd_init_window_size,
            "bwd_init_window_size":     self.bwd_init_window_size,
            "fwd_last_window_size":     self.fwd_last_window_size,
            "payload_bytes_per_second": self.payload_bytes_per_second,
            "fwd_subflow_bytes":        self.fwd_subflow_bytes,
            "fwd_header_size_tot":      self.fwd_header_size_tot,
            "active_avg":               self.active_avg,
            "active_tot":               self.active_tot,
            "active_min":               self.active_min,
            "id_resp_p":                self.id_resp_p,
            "bwd_pkts_per_sec":         self.bwd_pkts_per_sec,
            "Attack_grouped":           self.Attack_grouped,
        }