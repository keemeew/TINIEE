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
        NoAction;
    }
    default_action = NoAction;
    size = 126;
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
        NoAction;
    }
    default_action = NoAction;
    size = 126;
}

table tb_invalid{
    key = {
        hdr.tiniee.cnt: exact;
    }
    actions = {
        invalid_header;
        NoAction;
    }
    default_action = NoAction;
    size = 2;
}