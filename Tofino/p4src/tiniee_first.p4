/* -*- P4_16 -*- */
#include <core.p4>
#include <tna.p4>

#include "include/header.p4"
#include "include/parser.p4"


/*************************************************************************
************************  INGRESS  ****************************************
*************************************************************************/
control SwitchIngress(inout headers hdr, 
					  inout ingress_metadata_t ig_md, 
					  in ingress_intrinsic_metadata_t ig_intr_md, 
					  in ingress_intrinsic_metadata_from_parser_t ig_prsr_md, 
					  inout ingress_intrinsic_metadata_for_deparser_t ig_dprsr_md, 
		  			  inout ingress_intrinsic_metadata_for_tm_t ig_tm_md) {
    bit<8> c_threshold = 65;

    #include "include/ingress_action.p4"
    #include "include/ingress_table.p4"
    
    apply {
        if (hdr.ethernet.etherType == 0x0800) {
            tb_init.apply();
        }
        
        if (hdr.inference.isValid()) { 
            
            tb_weight_preprocessing.apply(); 
            tb_feature_preprocessing.apply();
            
            tb_XNOR_1.apply();
            tb_XNOR_2.apply();
            tb_XNOR_3_1.apply();
            tb_XNOR_3_2.apply();
            tb_XNOR_4_1.apply();
            tb_XNOR_4_2.apply();
            tb_XNOR_5.apply();
            tb_XNOR_6.apply();
            tb_XNOR_7.apply();

            tb_popcount1.apply();
            tb_popcount2.apply();
            tb_popcount3_1.apply();
            tb_popcount3_2.apply();
            tb_popcount4_1.apply();
            tb_popcount4_2.apply();
            tb_popcount5.apply();
            tb_popcount6.apply();
            tb_popcount7.apply();

            total_popcount1();
            total_popcount2();
            total_popcount3();
            total_popcount4();
            total_popcount5();
            total_popcount6();
            total_popcount7();
            total_popcount8();

            tb_set_spaces.apply();

            tb_substraction.apply();

            tb_predict.apply();

            tb_compute_confidence.apply();
            
            if (ig_md.meta.confidence >=c_threshold || hdr.inference.layer == 3){
                ig_md.meta.exit_result = 1;
            }
            else{
                ig_md.meta.exit_result = 0;
            }
        }

        if (hdr.tiniee.isValid()){
            tb_forward.apply();
        }
        else{
            tb_normal_forwarding.apply();
        }
    }
}

/*************************************************************************
*********************** E G R E S S  *************************************
*************************************************************************/
control SwitchEgress(inout headers hdr, 
					 inout egress_metadata_t eg_md, 
 					 in egress_intrinsic_metadata_t eg_intr_md, 
					 in egress_intrinsic_metadata_from_parser_t eg_prsr_md, 
					 inout egress_intrinsic_metadata_for_deparser_t eg_dprsr_md, 
					 inout egress_intrinsic_metadata_for_output_port_t eg_oport_md) {
    
    #include "include/egress_action.p4"
    #include "include/egress_table.p4"
    
    apply {
        tb_exit_process.apply();
        tb_activate_zero.apply();
        if (eg_md.meta.PopCountOut > 63){
            tb_activate_one.apply();
        }

        tb_invalid.apply();
     }
}

/*************************************************************************
*********************** SWITCH ********************************************
*************************************************************************/
Pipeline(SwitchIngressParser(),
	SwitchIngress(),
	SwitchIngressDeparser(),
	SwitchEgressParser(),
	SwitchEgress(),
	SwitchEgressDeparser()
) pipe;

Switch(pipe) main;