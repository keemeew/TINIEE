/* -*- P4_16 -*- */
#include <core.p4>
#include <v1model.p4>
/* CONSTANTS */
const bit<16> TYPE_IPV4 = 0x800;
const bit<16> TYPE_INFER = 0x8845;
const bit<8>  TYPE_TCP  = 6;
const bit<16> Type_Exit = 0x8890;
// #define CONST_MAX_PORTS 	32
// #define CONST_MAX_LABELS 	10
// #define REGISTER_LENGTH 255
/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/
typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;
typedef bit<13> switch_id_t;
header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16>   etherType;
}
header inference_t {
    bit<126>    val;
    bit<2>      flag;
    bit<48>     enter_time;
    bit<48>     exit_time;
}
header ipv4_t {
    bit<4>    version;
    bit<4>    ihl;
    bit<8>    tos;
    bit<16>   totalLen;
    bit<16>   identification;
    bit<3>    flags;
    bit<13>   fragOffset;
    bit<8>    ttl;
    bit<8>    protocol;
    bit<16>   hdrChecksum;
    ip4Addr_t srcAddr;
    ip4Addr_t dstAddr;
}
header tcp_t {
    bit<16> srcPort;
    bit<16> dstPort;
    bit<32> seqNo;
    bit<32> ackNo;
    bit<4>  dataOffset;
    bit<3>  res;
    bit<3>  ecn;
    bit<6>  ctrl;
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr;
}
header udp_t {
    bit<16> srcPort;
    bit<16> dstPort;
    bit<16> length_;
    bit<16> checksum;
}
struct headers {
    ethernet_t          ethernet;
    inference_t             inference;
    ipv4_t              ipv4;
    tcp_t               tcp;
    udp_t               udp;
}
struct metadata {
    bit<1> is_ingress_border;
    bit<1> is_egress_border;
    bit<1> activated_exit_1;
    bit<1> activated_exit_2;
    bit<13> swid;
    bit<2> flag;
}
/*************************************************************************
*********************** P A R S E R  ***********************************
*************************************************************************/
parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {
    state start {
        packet.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType){
            TYPE_INFER: parse_inference;
            TYPE_IPV4: ipv4;
            Type_Exit: ipv4;
            default: accept;
        }
    }
    state parse_inference {
        packet.extract(hdr.inference);
        transition ipv4;
    }
    state ipv4 {
        packet.extract(hdr.ipv4);
        transition select(hdr.ipv4.protocol) {
            17: parse_udp;
            6:  parse_tcp;
            default: accept;
        }
    }
    state parse_tcp {
        packet.extract(hdr.tcp);
        transition accept;
    }
    state parse_udp {
        packet.extract(hdr.udp);
        transition accept;
    }
}
/*************************************************************************
************   C H E C K S U M    V E R I F I C A T I O N   *************
*************************************************************************/
control MyVerifyChecksum(inout headers hdr, inout metadata meta) {
    apply {  }
}
/*************************************************************************
**************  I N G R E S S   P R O C E S S I N G   *******************
*************************************************************************/
control MyIngress(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {

    action set_egress_port_normal(bit<9> port){ // destination = destination node
        standard_metadata.egress_spec = port;
        hdr.ipv4.ttl=hdr.ipv4.ttl-1;
    }

    action set_egress_port_inference(bit<9> port){ // destination = destination node
        standard_metadata.egress_spec = port;
        hdr.ipv4.ttl=hdr.ipv4.ttl-1;
    }

    action report_missing() {
        // Print a message or take some action to indicate a missing entry
        // This is a placeholder; actual implementation depends on the P4 target
        standard_metadata.egress_spec = 0;
    }
    table address_check {
        key = {
            hdr.inference.flag: exact;
            hdr.ipv4.srcAddr: exact;
            hdr.ipv4.dstAddr: exact;
        
            meta.flag: exact;
        }
        actions = {
            
            NoAction;
        }
        default_action = NoAction();
    }
    table tb_normal_forwarding{
        key = {
            hdr.ipv4.dstAddr: exact;
        }
        actions = {
            set_egress_port_normal;
            report_missing;//NoAction;
        }
        const default_action = report_missing();
    }

    table tb_inference_forwarding{
        key = {
            meta.flag: exact;
        }
        actions = {
            set_egress_port_inference;
            NoAction;
        }
        size = 2000;
        
        const default_action = NoAction();
    }
    table tb_inference_forwarding2{
        key = {
            meta.flag: exact;
        }
        actions = {
            set_egress_port_inference;
            NoAction;
        }
        size = 2000;
        
        const default_action = NoAction();
    }


    apply {
        meta.flag = 0;
        meta.flag = hdr.inference.flag;
        address_check.apply();
        
        
        
        
        if (hdr.ethernet.etherType == Type_Exit){
            tb_normal_forwarding.apply();
        }
        else{

            tb_inference_forwarding.apply();




    }
    }
}
/*************************************************************************
****************  E G R E S S   P R O C E S S I N G   *******************
*************************************************************************/
control MyEgress(inout headers hdr,
                 inout metadata meta,
                 inout standard_metadata_t standard_metadata) {
    apply {
        // hdr.inference.exit_time = standard_metadata.egress_global_timestamp;
    }
}
/*************************************************************************
*************   C H E C K S U M    C O M P U T A T I O N   **************
*************************************************************************/
control MyComputeChecksum(inout headers hdr, inout metadata meta) {
     apply {
	update_checksum(
	    hdr.ipv4.isValid(),
            { hdr.ipv4.version,
	      hdr.ipv4.ihl,
              hdr.ipv4.tos,
              hdr.ipv4.totalLen,
              hdr.ipv4.identification,
              hdr.ipv4.flags,
              hdr.ipv4.fragOffset,
              hdr.ipv4.ttl,
              hdr.ipv4.protocol,
              hdr.ipv4.srcAddr,
              hdr.ipv4.dstAddr },
            hdr.ipv4.hdrChecksum,
            HashAlgorithm.csum16);
    }
}
/*************************************************************************
***********************  D E P A R S E R  *******************************
*************************************************************************/
control MyDeparser(packet_out packet, in headers hdr) {
    apply {
        //parsed headers have to be added again into the packet.
        packet.emit(hdr.ethernet);
        packet.emit(hdr.inference);
        packet.emit(hdr.ipv4);
        packet.emit(hdr.tcp);
        packet.emit(hdr.udp);
    }
}
/*************************************************************************
***********************  S W I T C H  *******************************
*************************************************************************/
//switch architecture
V1Switch(
MyParser(),
MyVerifyChecksum(),
MyIngress(),
MyEgress(),
MyComputeChecksum(),
MyDeparser()
) main;
