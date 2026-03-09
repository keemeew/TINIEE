action weight_preprocessing(bit<16> weight_1, bit<8> weight_2, 
                            bit<16> weight_3_1, bit<16> weight_3_2,
                            bit<16> weight_4_1, bit<16> weight_4_2, 
                            bit<16> weight_5, bit<16> weight_6, 
                            bit<8> weight_7) {
    ig_md.meta.weight_1 = weight_1;
    ig_md.meta.weight_2 = weight_2;
    ig_md.meta.weight_3_1 = weight_3_1;
    ig_md.meta.weight_3_2 = weight_3_2;
    ig_md.meta.weight_4_1 = weight_4_1;
    ig_md.meta.weight_4_2 = weight_4_2;
    ig_md.meta.weight_5 = weight_5;
    ig_md.meta.weight_6 = weight_6;
    ig_md.meta.weight_7 = weight_7;
}

action XNOR_1_1() {
    ig_md.meta.XNOROutput_1 = ~(ig_md.meta.weight_1 ^ hdr.inference.features_1);
}

action XNOR_1_2() {
    ig_md.meta.XNOROutput_2 = ~(ig_md.meta.weight_2 ^ hdr.inference.features_2);
}

action XNOR_1_3_1() {
    ig_md.meta.XNOROutput_3_1 = ~(ig_md.meta.weight_3_1 ^ hdr.inference.features_3_1);
}

action XNOR_1_3_2() {
    ig_md.meta.XNOROutput_3_2 = ~(ig_md.meta.weight_3_2 ^ hdr.inference.features_3_2);
}

action XNOR_1_4_1() {
    ig_md.meta.XNOROutput_4_1 = ~(ig_md.meta.weight_4_1 ^ hdr.inference.features_4_1);
}

action XNOR_1_4_2() {
    ig_md.meta.XNOROutput_4_2 = ~(ig_md.meta.weight_4_2 ^ hdr.inference.features_4_2);
}

action XNOR_1_5() {
    ig_md.meta.XNOROutput_5 = ~(ig_md.meta.weight_5 ^ hdr.inference.features_5);
}

action XNOR_1_6() {
    ig_md.meta.XNOROutput_6 = ~(ig_md.meta.weight_6 ^ hdr.inference.features_6);
}

action XNOR_1_7() {
    ig_md.meta.XNOROutput_7 = ~(ig_md.meta.weight_7 ^ hdr.inference.features_7);
}

action XNOR_2_1() {
    ig_md.meta.XNOROutput_1 = ~(ig_md.meta.weight_1 ^ hdr.intermediate_data.intermediate_data_1);
}

action XNOR_2_2() {
    ig_md.meta.XNOROutput_2 = ~(ig_md.meta.weight_2 ^ hdr.intermediate_data.intermediate_data_2);
}

action XNOR_2_3_1() {
    ig_md.meta.XNOROutput_3_1 = ~(ig_md.meta.weight_3_1 ^ hdr.intermediate_data.intermediate_data_3_1);
}

action XNOR_2_3_2() {
    ig_md.meta.XNOROutput_3_2 = ~(ig_md.meta.weight_3_2 ^ hdr.intermediate_data.intermediate_data_3_2);
}

action XNOR_2_4_1() {
    ig_md.meta.XNOROutput_4_1 = ~(ig_md.meta.weight_4_1 ^ hdr.intermediate_data.intermediate_data_4_1);
}

action XNOR_2_4_2() {
    ig_md.meta.XNOROutput_4_2 = ~(ig_md.meta.weight_4_2 ^ hdr.intermediate_data.intermediate_data_4_2);
}

action XNOR_2_5() {
    ig_md.meta.XNOROutput_5 = ~(ig_md.meta.weight_5 ^ hdr.intermediate_data.intermediate_data_5);
}

action XNOR_2_6() {
    ig_md.meta.XNOROutput_6 = ~(ig_md.meta.weight_6 ^ hdr.intermediate_data.intermediate_data_6);
}

action XNOR_2_7() {
    ig_md.meta.XNOROutput_7 = ~(ig_md.meta.weight_7 ^ hdr.intermediate_data.intermediate_data_7);
}

action popcount1(bit<8> x){
    ig_md.meta.x_1 = x;
}
action popcount2(bit<8> x){
    ig_md.meta.x_2 = x;
}
action popcount3_1(bit<8> x){
    ig_md.meta.x_3_1 = x;
}
action popcount3_2(bit<8> x){
    ig_md.meta.x_3_2 = x;
}
action popcount4_1(bit<8> x){
    ig_md.meta.x_4_1 = x;
}
action popcount4_2(bit<8> x){
    ig_md.meta.x_4_2 = x;
}
action popcount5(bit<8> x){
    ig_md.meta.x_5 = x;
}
action popcount6(bit<8> x){
    ig_md.meta.x_6 = x;
}
action popcount7(bit<8> x){
    ig_md.meta.x_7 = x;
}

action total_popcount1(){
    ig_md.meta.PopCountOut = ig_md.meta.x_1 + ig_md.meta.x_2;
}
action total_popcount2(){
    ig_md.meta.PopCountOut = ig_md.meta.PopCountOut + ig_md.meta.x_3_1;
}
action total_popcount3(){
    ig_md.meta.PopCountOut = ig_md.meta.PopCountOut + ig_md.meta.x_3_2;
}
action total_popcount4(){
    ig_md.meta.PopCountOut = ig_md.meta.PopCountOut + ig_md.meta.x_4_1;
}
action total_popcount5(){
    ig_md.meta.PopCountOut = ig_md.meta.PopCountOut + ig_md.meta.x_4_2;
}
action total_popcount6(){
    ig_md.meta.PopCountOut = ig_md.meta.PopCountOut + ig_md.meta.x_5;
}
action total_popcount7(){
    ig_md.meta.PopCountOut = ig_md.meta.PopCountOut + ig_md.meta.x_6;
}
action total_popcount8(){
    ig_md.meta.PopCountOut = ig_md.meta.PopCountOut + ig_md.meta.x_7;
}

action set_intermediate_data(){ 
    hdr.intermediate_data.setValid();
    hdr.ipv4.totalLen = hdr.ipv4.totalLen + 16;
}

action one_to_big(){
    ig_md.meta.big_number = hdr.tiniee.PopCount1;
    ig_md.meta.small_number = hdr.tiniee.PopCount2;
    hdr.ipv4.tos[1:0] = 0;
}

action one_to_small(){
    ig_md.meta.big_number = hdr.tiniee.PopCount2;
    ig_md.meta.small_number = hdr.tiniee.PopCount1;
    hdr.ipv4.tos[1:0] = 1;
}

action substraction(){
    ig_md.meta.substract = hdr.tiniee.PopCount1 - hdr.tiniee.PopCount2;
}

action inference_routing(bit<9> egress_spec) {
    ig_tm_md.ucast_egress_port = egress_spec;
    hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
    hdr.tiniee.cnt = hdr.tiniee.cnt + 1;
    hdr.ipv4.tos[7:2] = 10;
}

action do_recirculation() {
    ig_tm_md.ucast_egress_port = 68;
    hdr.tiniee.cnt = hdr.tiniee.cnt + 1;
    
}

action set_egress_port(bit<9> egress_spec) {
    ig_tm_md.ucast_egress_port = egress_spec;
    hdr.ipv4.ttl=hdr.ipv4.ttl-1;
}