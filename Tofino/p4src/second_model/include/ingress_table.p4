table tb_weight_preprocessing{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        weight_preprocessing; 
        NoAction;
    }
    default_action = NoAction;
    size = 254;
}

table tb_XNOR_1{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_1;
        XNOR_2_1;
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_XNOR_2{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_2;
        XNOR_2_2;
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_XNOR_3_1{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_3_1;
        XNOR_2_3_1;
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_XNOR_3_2{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_3_2;
        XNOR_2_3_2;
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_XNOR_4_1{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_4_1; 
        XNOR_2_4_1; 
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_XNOR_4_2{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_4_2; 
        XNOR_2_4_2; 
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_XNOR_5{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_5; 
        XNOR_2_5; 
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_XNOR_6{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_6; 
        XNOR_2_6; 
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_XNOR_7{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        XNOR_1_7; 
        XNOR_2_7; 
        NoAction;
    }
    default_action = NoAction;
    size = 128;
}

table tb_popcount1 {
    key = {
        ig_md.meta.XNOROutput_1: exact;
    }
    actions = {
        popcount1();
        NoAction;
    }
    default_action = NoAction;
    size = 65536;
}

table tb_popcount2 {
    key = {
        ig_md.meta.XNOROutput_2: exact;
    }
    actions = {
        popcount2();
        NoAction;
    }
    default_action = NoAction;
    size = 256;
}

table tb_popcount3_1 {
    key = {
        ig_md.meta.XNOROutput_3_1: exact;
    }
    actions = {
        popcount3_1();
        NoAction;
    }
    default_action = NoAction;
    size = 65536;
}

table tb_popcount3_2 {
    key = {
        ig_md.meta.XNOROutput_3_2: exact;
    }
    actions = {
        popcount3_2();
        NoAction;
    }
    default_action = NoAction;
    size = 65536;
}

table tb_popcount4_1 {
    key = {
        ig_md.meta.XNOROutput_4_1: exact;
    }
    actions = {
        popcount4_1();
        NoAction;
    }
    default_action = NoAction;
    size = 65536;
}

table tb_popcount4_2 {
    key = {
        ig_md.meta.XNOROutput_4_2: exact;
    }
    actions = {
        popcount4_2();
        NoAction;
    }
    default_action = NoAction;
    size = 65536;
}

table tb_popcount5 {
    key = {
        ig_md.meta.XNOROutput_5: exact;
    }
    actions = {
        popcount5();
        NoAction;
    }
    default_action = NoAction;
    size = 65536;
}

table tb_popcount6 {
    key = {
        ig_md.meta.XNOROutput_6: exact;
    }
    actions = {
        popcount6();
        NoAction;
    }
    default_action = NoAction;
    size = 65536;
}

table tb_popcount7 {
    key = {
        ig_md.meta.XNOROutput_7: exact;
    }
    actions = {
        popcount7();
        NoAction;
    }
    default_action = NoAction;
    size = 256;
}

table tb_set_spaces{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        set_intermediate_data; 
        NoAction;
    }
    default_action = NoAction;
    size = 1;
}

table tb_substraction {
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        substraction;
        NoAction;
    }
    size = 1;
    default_action = NoAction;
}

table tb_predict{
    key = {
        hdr.tiniee.cnt: exact;
        ig_md.meta.substract: ternary; 
    }
    actions = {
        one_to_big;
        one_to_small;
        NoAction;
    }
    default_action = NoAction;
    size = 2;
}

table tb_compute_confidence {
    key = {
        ig_md.meta.small_number: exact;
        ig_md.meta.big_number: range;
    }
    actions = {
        early_exit_flag;
    }
    size = 3367;
    const entries = {
        #include "confidence_score.p4"
    }
}

table tb_forward {
	key = {
        ig_md.meta.exit_result: exact;
        hdr.tiniee.cnt: exact; 
	}
	actions = {
        early_exit;
        inference_routing;
        do_recirculation;
		NoAction();
	}
	default_action = NoAction();
    size = 130;
}

table tb_normal_forwarding {
    key = {
        ig_intr_md.ingress_port: exact;
    }
    actions = {
        set_egress_port;
        NoAction;
    }
    const default_action = NoAction();
    size = 1;
}