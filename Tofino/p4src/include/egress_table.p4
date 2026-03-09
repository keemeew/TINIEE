table tb_exit_process{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        exit_process1; 
        exit_process2; 
        NoAction;
    }
    default_action = NoAction;
    size =2;
}

table tb_activate_zero {
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        activate_1_zero; 
        activate_2_zero; 
        activate_3_1_zero; 
        activate_3_2_zero; 
        activate_4_1_zero; 
        activate_4_2_zero; 
        activate_5_zero; 
        activate_6_zero; 
        activate_7_zero; 
        activate_1_zero_2; 
        activate_2_zero_2; 
        activate_3_1_zero_2; 
        activate_3_2_zero_2; 
        activate_4_1_zero_2; 
        activate_4_2_zero_2; 
        activate_5_zero_2; 
        activate_6_zero_2; 
        activate_7_zero_2; 
        NoAction;
    }
    default_action = NoAction;
    size = 252;
}

table tb_activate_one {
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        activate_1_one; 
        activate_2_one; 
        activate_3_1_one; 
        activate_3_2_one; 
        activate_4_1_one; 
        activate_4_2_one; 
        activate_5_one; 
        activate_6_one; 
        activate_7_one; 
        activate_1_one_2; 
        activate_2_one_2; 
        activate_3_1_one_2; 
        activate_3_2_one_2; 
        activate_4_1_one_2; 
        activate_4_2_one_2; 
        activate_5_one_2; 
        activate_6_one_2; 
        activate_7_one_2; 
        NoAction;
    }
    default_action = NoAction;
    size = 252;
}

table tb_invalid{
    key = {
        hdr.tiniee.cnt: exact;
        eg_md.meta.exit_result: exact;
    }
    actions = {
        invalid_header;
        early_exit;
        NoAction;
    }
    default_action = NoAction;
    size = 2;
}