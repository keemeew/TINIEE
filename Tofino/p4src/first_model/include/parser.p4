/*************************************************************************
********************  Ingress Parser  ************************************
*************************************************************************/

parser SwitchIngressParser(packet_in packet,
                           out headers hdr,
                           out ingress_metadata_t ig_md,
                           out ingress_intrinsic_metadata_t ig_intr_md)
{
    state start {
        packet.extract(ig_intr_md);
        packet.advance(PORT_METADATA_SIZE);

        transition parse_ethernet;
    }
    
    state parse_ethernet {
        packet.extract(hdr.ethernet);
        ig_md.meta.setValid();
        transition select(hdr.ethernet.etherType) {
            TYPE_INFER: parse_inference;
            TYPE_IPV4: parse_ipv4;
            Type_Exit: parse_inference;
            default: accept;
        }
    }

    state parse_inference {
        packet.extract(hdr.ipv4);
        packet.extract(hdr.inference);
        transition select(hdr.ipv4.tos[7:2]){
            20: parse_intermediate_data;
            default: parse_tcp;
        }
    }

    state parse_ipv4 {
        packet.extract(hdr.ipv4);
        transition select(hdr.ipv4.protocol) {
            6: parse_tcp;
            default: accept;
        }
    }

    state parse_intermediate_data {
        packet.extract(hdr.tiniee);
        packet.extract(hdr.intermediate_data);
        transition parse_tcp;
    }
    state parse_tcp {
        packet.extract(hdr.tcp);
        transition accept;
    }

}

/*************************************************************************
*******************  Ingress Deparser  ***********************************
*************************************************************************/

control SwitchIngressDeparser(packet_out packet, 
                             inout headers hdr,
                             in ingress_metadata_t ig_md,
                             in ingress_intrinsic_metadata_for_deparser_t ig_dprsr_md) {
		apply {
            packet.emit(ig_md.meta);
            packet.emit(hdr);
		}
}

/*************************************************************************
********************* Egress Parser **************************************
*************************************************************************/
/* parse ethernet -> ipv4 -> tcp/udp -> labeling_t */
parser SwitchEgressParser(packet_in packet,
                          out headers hdr,
                          out egress_metadata_t eg_md, 
                          out egress_intrinsic_metadata_t eg_intr_md) {
    state start {
        packet.extract(eg_intr_md);
        packet.extract(eg_md.meta);
        
        transition parse_ethernet;
    }
    
    state parse_ethernet {
        packet.extract(hdr.ethernet);
        eg_md.meta.setValid();
        transition select(hdr.ethernet.etherType) {
            TYPE_INFER: parse_inference;
            TYPE_IPV4: parse_ipv4;
            Type_Exit: parse_inference;
            default: accept;
        }
    }

    state parse_inference {
        packet.extract(hdr.ipv4);
        packet.extract(hdr.inference);
        transition select(hdr.ipv4.tos[7:2]){
            20: parse_intermediate_data;
            default: parse_tcp;
            
        }
    }

    state parse_ipv4 {
        packet.extract(hdr.ipv4);
        transition select(hdr.ipv4.protocol) {
            6: parse_tcp;
            default: accept;
        }
    }

    state parse_intermediate_data {
        packet.extract(hdr.tiniee);
        packet.extract(hdr.intermediate_data);
        transition parse_tcp;
    }
    state parse_tcp {
        packet.extract(hdr.tcp);
        transition accept;
    }
}

/*************************************************************************
******************** Egress Deparser *************************************
*************************************************************************/

control SwitchEgressDeparser(packet_out packet, 
                             inout headers hdr,
                             in egress_metadata_t eg_md, 
                             in egress_intrinsic_metadata_for_deparser_t eg_dprsr_md) {
		apply {
            packet.emit(hdr.ethernet);
            packet.emit(hdr.ipv4);
            packet.emit(hdr.inference);
            packet.emit(hdr.tiniee);
            packet.emit(hdr.intermediate_data);
            packet.emit(hdr.tcp);
		}
}