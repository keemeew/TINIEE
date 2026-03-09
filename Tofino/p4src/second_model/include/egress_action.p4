action exit_process1(){
    hdr.tiniee.PopCount1 = eg_md.meta.PopCountOut;
}

action exit_process2(){
    hdr.tiniee.PopCount2 = eg_md.meta.PopCountOut;
}

action activate_1_zero(){
    hdr.intermediate_data.intermediate_data_1 = hdr.intermediate_data.intermediate_data_1 << 1;
}
action activate_2_zero(){
    hdr.intermediate_data.intermediate_data_2 = hdr.intermediate_data.intermediate_data_2 << 1;
}
action activate_3_1_zero(){
    hdr.intermediate_data.intermediate_data_3_1 = hdr.intermediate_data.intermediate_data_3_1 << 1;
}
action activate_3_2_zero(){
    hdr.intermediate_data.intermediate_data_3_2 = hdr.intermediate_data.intermediate_data_3_2 << 1;
}
action activate_4_1_zero(){
    hdr.intermediate_data.intermediate_data_4_1 = hdr.intermediate_data.intermediate_data_4_1 << 1;
}
action activate_4_2_zero(){
    hdr.intermediate_data.intermediate_data_4_2 = hdr.intermediate_data.intermediate_data_4_2 << 1;
}
action activate_5_zero(){
    hdr.intermediate_data.intermediate_data_5 = hdr.intermediate_data.intermediate_data_5 << 1;
}
action activate_6_zero(){
    hdr.intermediate_data.intermediate_data_6 = hdr.intermediate_data.intermediate_data_6 << 1;
}
action activate_7_zero(){
    hdr.intermediate_data.intermediate_data_7 = hdr.intermediate_data.intermediate_data_7 << 1;
}

action activate_1_one(){
    hdr.intermediate_data.intermediate_data_1 = hdr.intermediate_data.intermediate_data_1 + 1;
}
action activate_2_one(){
    hdr.intermediate_data.intermediate_data_2 = hdr.intermediate_data.intermediate_data_2 + 1;
}
action activate_3_1_one(){
    hdr.intermediate_data.intermediate_data_3_1 = hdr.intermediate_data.intermediate_data_3_1 + 1;
}
action activate_3_2_one(){
    hdr.intermediate_data.intermediate_data_3_2 = hdr.intermediate_data.intermediate_data_3_2 + 1;
}
action activate_4_1_one(){
    hdr.intermediate_data.intermediate_data_4_1 = hdr.intermediate_data.intermediate_data_4_1 + 1;
}
action activate_4_2_one(){
    hdr.intermediate_data.intermediate_data_4_2 = hdr.intermediate_data.intermediate_data_4_2 + 1;
}
action activate_5_one(){
    hdr.intermediate_data.intermediate_data_5 = hdr.intermediate_data.intermediate_data_5 + 1;
}
action activate_6_one(){
    hdr.intermediate_data.intermediate_data_6 = hdr.intermediate_data.intermediate_data_6 + 1;
}
action activate_7_one(){
    hdr.intermediate_data.intermediate_data_7 = hdr.intermediate_data.intermediate_data_7 + 1;
}

action invalid_header(){
    hdr.intermediate_data.setInvalid();
    hdr.tiniee.setInvalid();
}

action early_exit(){
    hdr.intermediate_data.setInvalid();
    hdr.tiniee.setInvalid();
    hdr.inference.setInvalid();
}