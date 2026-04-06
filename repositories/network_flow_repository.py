from extensions import db
from models.mlservice import MLService
from models.networkflows import NetworkFlow

_ml_service = MLService() # Global instance of MLService to avoid reloading models on every analyze call

class NetworkFlowRepository:

    def get_all(self):
        return NetworkFlow.query.all()

    def get_by_id(self, id):
        return NetworkFlow.query.get(id)

    def create(self, data):
        flow = NetworkFlow(
            proto                   = data.get('proto'),
            service                 = data.get('service'),
            flow_duration           = data.get('flow_duration'),
            fwd_pkts_tot            = data.get('fwd_pkts_tot'),
            bwd_pkts_tot            = data.get('bwd_pkts_tot'),
            flow_pkts_per_sec       = data.get('flow_pkts_per_sec'),
            down_up_ratio           = data.get('down_up_ratio'),
            flow_FIN_flag_count     = data.get('flow_FIN_flag_count'),
            flow_SYN_flag_count     = data.get('flow_SYN_flag_count'),
            flow_RST_flag_count     = data.get('flow_RST_flag_count'),
            flow_ACK_flag_count     = data.get('flow_ACK_flag_count'),
            fwd_pkts_payload_avg    = data.get('fwd_pkts_payload_avg'),
            bwd_pkts_payload_avg    = data.get('bwd_pkts_payload_avg'),
            fwd_pkts_payload_tot    = data.get('fwd_pkts_payload_tot'),
            fwd_pkts_payload_min    = data.get('fwd_pkts_payload_min'),
            flow_pkts_payload_avg   = data.get('flow_pkts_payload_avg'),
            flow_pkts_payload_std   = data.get('flow_pkts_payload_std'),
            fwd_iat_avg             = data.get('fwd_iat_avg'),
            bwd_iat_avg             = data.get('bwd_iat_avg'),
            flow_iat_avg            = data.get('flow_iat_avg'),
            fwd_init_window_size    = data.get('fwd_init_window_size'),
            bwd_init_window_size    = data.get('bwd_init_window_size'),
            fwd_last_window_size    = data.get('fwd_last_window_size'),
            payload_bytes_per_second= data.get('payload_bytes_per_second'),
            fwd_subflow_bytes       = data.get('fwd_subflow_bytes'),
            fwd_header_size_tot     = data.get('fwd_header_size_tot'),
            active_avg              = data.get('active_avg'),
            active_tot              = data.get('active_tot'),
            active_min              = data.get('active_min'),
            id_resp_p               = data.get('id_resp_p'),
            bwd_pkts_per_sec        = data.get('bwd_pkts_per_sec'),
            Attack_grouped          = data.get('Attack_grouped'),
        )
        db.session.add(flow)
        db.session.commit()
        return flow

    def update(self, id, data):
        flow = NetworkFlow.query.get(id)
        if not flow:
            return None

        updatable_fields = [
            'proto', 'service', 'flow_duration', 'fwd_pkts_tot', 'bwd_pkts_tot',
            'flow_pkts_per_sec', 'down_up_ratio', 'flow_FIN_flag_count',
            'flow_SYN_flag_count', 'flow_RST_flag_count', 'flow_ACK_flag_count',
            'fwd_pkts_payload_avg', 'bwd_pkts_payload_avg', 'fwd_pkts_payload_tot',
            'fwd_pkts_payload_min', 'flow_pkts_payload_avg', 'flow_pkts_payload_std',
            'fwd_iat_avg', 'bwd_iat_avg', 'flow_iat_avg', 'fwd_init_window_size',
            'bwd_init_window_size', 'fwd_last_window_size', 'payload_bytes_per_second',
            'fwd_subflow_bytes', 'fwd_header_size_tot', 'active_avg', 'active_tot',
            'active_min', 'id_resp_p', 'bwd_pkts_per_sec', 'Attack_grouped'
        ]

        for field in updatable_fields:
            if field in data:
                setattr(flow, field, data[field])

        db.session.commit()
        return flow

    def delete(self, id):
        flow = NetworkFlow.query.get(id)
        if not flow:
            return False
        db.session.delete(flow)
        db.session.commit()
        return True
    
    def analyze(self, data):
        selected_model = data.get('model') 
        
        flow = NetworkFlow(
            proto                    = data.get('proto'),
            service                  = data.get('service'),
            flow_duration            = data.get('flow_duration'),
            fwd_pkts_tot             = data.get('fwd_pkts_tot'),
            bwd_pkts_tot             = data.get('bwd_pkts_tot'),
            flow_pkts_per_sec        = data.get('flow_pkts_per_sec'),
            down_up_ratio            = data.get('down_up_ratio'),
            flow_FIN_flag_count      = data.get('flow_FIN_flag_count'),
            flow_SYN_flag_count      = data.get('flow_SYN_flag_count'),
            flow_RST_flag_count      = data.get('flow_RST_flag_count'),
            flow_ACK_flag_count      = data.get('flow_ACK_flag_count'),
            fwd_pkts_payload_avg     = data.get('fwd_pkts_payload_avg'),
            bwd_pkts_payload_avg     = data.get('bwd_pkts_payload_avg'),
            fwd_pkts_payload_tot     = data.get('fwd_pkts_payload_tot'),
            fwd_pkts_payload_min     = data.get('fwd_pkts_payload_min'),
            flow_pkts_payload_avg    = data.get('flow_pkts_payload_avg'),
            flow_pkts_payload_std    = data.get('flow_pkts_payload_std'),
            fwd_iat_avg              = data.get('fwd_iat_avg'),
            bwd_iat_avg              = data.get('bwd_iat_avg'),
            flow_iat_avg             = data.get('flow_iat_avg'),
            fwd_init_window_size     = data.get('fwd_init_window_size'),
            bwd_init_window_size     = data.get('bwd_init_window_size'),
            fwd_last_window_size     = data.get('fwd_last_window_size'),
            payload_bytes_per_second = data.get('payload_bytes_per_second'),
            fwd_subflow_bytes        = data.get('fwd_subflow_bytes'),
            fwd_header_size_tot      = data.get('fwd_header_size_tot'),
            active_avg               = data.get('active_avg'),
            active_tot               = data.get('active_tot'),
            active_min               = data.get('active_min'),
            id_resp_p                = data.get('id_resp_p'),
            bwd_pkts_per_sec         = data.get('bwd_pkts_per_sec'),
            Attack_grouped           = None  #data.get('Attack_grouped')
        )   
        results  = _ml_service.predict(flow, model_name=selected_model)      
        flow.Attack_grouped = results['prediction'] 

        db.session.add(flow)
        db.session.commit()
        return results 
        