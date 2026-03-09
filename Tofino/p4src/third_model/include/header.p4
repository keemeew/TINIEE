/* CONSTANTS */
const bit<16> TYPE_IPV4 = 0x800;
const bit<16> TYPE_INFER = 0x8845;
const bit<8>  TYPE_TCP  = 6;
const bit<16> Type_Exit = 0x8890;

/*************************************************************************
*********************** HEADERS ******************************************
*************************************************************************/

typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;
typedef bit<13> switch_id_t;

/* Ethernet */
header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16>   etherType;
}

header inference_t {
    bit<16> features_1;
    bit<8>  features_2;
    bit<16> features_3_1;
    bit<16> features_3_2;
    bit<16> features_4_1;
    bit<16> features_4_2;
    bit<16> features_5;    
    bit<16> features_6;
    bit<8>  features_7;
}

/* IPv4 */
header ipv4_t {
    bit<4>  version;
    bit<4>  ihl;
    bit<8>  tos;
    bit<16> totalLen;
    bit<16> identification;
    bit<3>  flags;
    bit<13> fragOffset;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> hdrChecksum;
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

header tiniee_t {
    bit<16> cnt;
    bit<8> flag;
    bit<8> PopCount1;
    bit<8> PopCount2;
}

header intermediate_data_t {
    bit<16> intermediate_data_1;
    bit<8> intermediate_data_2;
    bit<16> intermediate_data_3_1;
    bit<16> intermediate_data_3_2;
    bit<16> intermediate_data_4_1;
    bit<16> intermediate_data_4_2;
    bit<16> intermediate_data_5;    
    bit<16> intermediate_data_6;
    bit<8> intermediate_data_7;    
}

struct headers {
    ethernet_t ethernet;
    ipv4_t     ipv4;
    inference_t inference;
    tiniee_t   tiniee;
    intermediate_data_t intermediate_data;

    tcp_t      tcp;
}

/*************************************************************************
*********************** METADATA *****************************************
*************************************************************************/

header metadata_t {
    bit<16> XNOROutput_1;
    bit<8> XNOROutput_2;
    bit<16> XNOROutput_3_1;
    bit<16> XNOROutput_3_2;
    bit<16> XNOROutput_4_1;
    bit<16> XNOROutput_4_2;
    bit<16> XNOROutput_5;
    bit<16> XNOROutput_6;
    bit<8> XNOROutput_7;
    
    bit<16> weight_1;
    bit<8> weight_2;
    bit<16> weight_3_1;
    bit<16> weight_3_2;
    bit<16> weight_4_1;
    bit<16> weight_4_2;
    bit<16> weight_5;
    bit<16> weight_6;
    bit<8> weight_7;

    bit<8> test;
    bit<8> test2;
    
    bit<8> PopCountOut;
    bit<8> x_1;
    bit<8> x_2;
    bit<8> x_3_1;
    bit<8> x_3_2;
    bit<8> x_4_1;
    bit<8> x_4_2;
    bit<8> x_5;
    bit<8> x_6;
    bit<8> x_7;
    bit<8> x_8;

    bit<8> big_number;
    bit<8> small_number;
    bit<8> confidence;
    bit<8> substract;

    bit<6> padding;
    bit<1> flag;
    bit<1> exit_result;
}

struct ingress_metadata_t {
	metadata_t meta;
}

struct egress_metadata_t {
	metadata_t meta;
}