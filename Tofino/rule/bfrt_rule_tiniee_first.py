import csv
import re

def bits_to_int(bits):
    s = str(bits).strip()
    s = re.sub(r"\s+", "", s)
    if not s or any(c not in "01" for c in s):
        raise ValueError(f"Invalid bitstring: {bits!r}")
    return int(s, 2)

def load_csv_as_weights(csv_path):
    csv_file = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required = [f"col{i}" for i in range(1, 10)]
        missing = [c for c in required if c not in reader.fieldnames]
        if missing:
            raise KeyError(f"CSV header missing columns: {missing}. Got: {reader.fieldnames}")

        for row_idx, row in enumerate(reader, start=1):
            try:
                weights = [bits_to_int(row[f"col{i}"]) for i in range(1, 10)]
            except Exception as e:
                raise RuntimeError(f"Error parsing row {row_idx}: {e}. Row={row}") from e

            csv_file.append(weights)

    return csv_file

def popcount(v: int) -> int:
    try:
        return v.bit_count()
    except AttributeError:
        return bin(v).count("1")
    
#############################################################
################## Ingress pipeline rules ###################
#############################################################

p4_ingress = bfrt.tiniee_first.pipe.SwitchIngress

tb_init = p4_ingress.tb_init #

tb_weight_preprocessing = p4_ingress.tb_weight_preprocessing
tb_feature_preprocessing = p4_ingress.tb_feature_preprocessing #

tb_XNOR_1 = p4_ingress.tb_XNOR_1 #
tb_XNOR_2 = p4_ingress.tb_XNOR_2 #
tb_XNOR_3_1 = p4_ingress.tb_XNOR_3_1 #
tb_XNOR_3_2 = p4_ingress.tb_XNOR_3_2 #
tb_XNOR_4_1 = p4_ingress.tb_XNOR_4_1 #
tb_XNOR_4_2 = p4_ingress.tb_XNOR_4_2 #
tb_XNOR_5 = p4_ingress.tb_XNOR_5 #
tb_XNOR_6 = p4_ingress.tb_XNOR_6 #
tb_XNOR_7 = p4_ingress.tb_XNOR_7 #

tb_popcount1 = p4_ingress.tb_popcount1 #
tb_popcount2 = p4_ingress.tb_popcount2 #
tb_popcount3_1 = p4_ingress.tb_popcount3_1 #
tb_popcount3_2 = p4_ingress.tb_popcount3_2 #
tb_popcount4_1 = p4_ingress.tb_popcount4_1 #
tb_popcount4_2 = p4_ingress.tb_popcount4_2 #
tb_popcount5 = p4_ingress.tb_popcount5 #
tb_popcount6 = p4_ingress.tb_popcount6 #
tb_popcount7 = p4_ingress.tb_popcount7 #

tb_set_spaces = p4_ingress.tb_set_spaces #

tb_substraction = p4_ingress.tb_substraction #

tb_predict = p4_ingress.tb_predict #

tb_forward = p4_ingress.tb_forward #

csv_file = load_csv_as_weights("~/tiniee/p4src/weights.csv")
for i, weight in enumerate(csv_file):
    # 0~251
    if i >= 252:
        continue
    tb_weight_preprocessing.add_with_weight_preprocessing(
        cnt = i,
        weight_1 = weight[0],
        weight_2 = weight[1],
        weight_3_1 = weight[2],
        weight_3_2 = weight[3],
        weight_4_1 = weight[4],
        weight_4_2 = weight[5],
        weight_5 = weight[6],
        weight_6 = weight[7],
        weight_7 = weight[8]
    )

csv_file = load_csv_as_weights("~/tiniee/p4src/weights_exit.csv")
for i, weight in enumerate(csv_file):
    # 252,253
    if i >= 2:
        continue
    tb_weight_preprocessing.add_with_weight_preprocessing(
        cnt = i+252,
        weight_1 = weight[0],
        weight_2 = weight[1],
        weight_3_1 = weight[2],
        weight_3_2 = weight[3],
        weight_4_1 = weight[4],
        weight_4_2 = weight[5],
        weight_5 = weight[6],
        weight_6 = weight[7],
        weight_7 = weight[8]
    )

tb_feature_preprocessing.add_with_feature_preprocessing(
    cnt = 0
)

for i in range(0,126):
    tb_XNOR_1.add_with_XNOR_1_1(
        cnt=i
    )
    tb_XNOR_2.add_with_XNOR_1_2(
        cnt=i
    )
    tb_XNOR_3_1.add_with_XNOR_1_3_1(
        cnt=i
    )
    tb_XNOR_3_2.add_with_XNOR_1_3_2(
        cnt=i
    )
    tb_XNOR_4_1.add_with_XNOR_1_4_1(
        cnt=i
    )
    tb_XNOR_4_2.add_with_XNOR_1_4_2(
        cnt=i
    )
    tb_XNOR_5.add_with_XNOR_1_5(
        cnt=i
    )
    tb_XNOR_6.add_with_XNOR_1_6(
        cnt=i
    )
    tb_XNOR_7.add_with_XNOR_1_7(
        cnt=i
    )

for i in range(126,252):
    tb_XNOR_1.add_with_XNOR_2_1(
        cnt=i
    )
    tb_XNOR_2.add_with_XNOR_2_2(
        cnt=i
    )
    tb_XNOR_3_1.add_with_XNOR_2_3_1(
        cnt=i
    )
    tb_XNOR_3_2.add_with_XNOR_2_3_2(
        cnt=i
    )
    tb_XNOR_4_1.add_with_XNOR_2_4_1(
        cnt=i
    )
    tb_XNOR_4_2.add_with_XNOR_2_4_2(
        cnt=i
    )
    tb_XNOR_5.add_with_XNOR_2_5(
        cnt=i
    )
    tb_XNOR_6.add_with_XNOR_2_6(
        cnt=i
    )
    tb_XNOR_7.add_with_XNOR_2_7(
        cnt=i
    )

for i in range(252,254):
    tb_XNOR_1.add_with_XNOR_1_1(
        cnt=i
    )
    tb_XNOR_2.add_with_XNOR_1_2(
        cnt=i
    )
    tb_XNOR_3_1.add_with_XNOR_1_3_1(
        cnt=i
    )
    tb_XNOR_3_2.add_with_XNOR_1_3_2(
        cnt=i
    )
    tb_XNOR_4_1.add_with_XNOR_1_4_1(
        cnt=i
    )
    tb_XNOR_4_2.add_with_XNOR_1_4_2(
        cnt=i
    )
    tb_XNOR_5.add_with_XNOR_1_5(
        cnt=i
    )
    tb_XNOR_6.add_with_XNOR_1_6(
        cnt=i
    )
    tb_XNOR_7.add_with_XNOR_1_7(
        cnt=i
    )


for i in range(65536):
    tb_popcount1.add_with_popcount1(
        XNOROutput_1 = i,
        x = popcount(i)
    )
    tb_popcount3_1.add_with_popcount3_1(
        XNOROutput_3_1 = i,
        x = popcount(i)
    )
    tb_popcount3_2.add_with_popcount3_2(
        XNOROutput_3_2 = i,
        x = popcount(i)
    )
    tb_popcount4_1.add_with_popcount4_1(
        XNOROutput_4_1 = i,
        x = popcount(i)
    )
    tb_popcount4_2.add_with_popcount4_2(
        XNOROutput_4_2 = i,
        x = popcount(i)
    )
    tb_popcount5.add_with_popcount5(
        XNOROutput_5 = i,
        x = popcount(i)
    )
    tb_popcount6.add_with_popcount6(
        XNOROutput_6 = i,
        x = popcount(i)
    )

for i in range(256):
    tb_popcount2.add_with_popcount2(
        XNOROutput_2 = i,
        x = popcount(i)
    )

for i in range(256):
    tb_popcount7.add_with_popcount7(
        XNOROutput_7 = i,
        x = popcount(i)
    )

tb_set_spaces.add_with_set_intermediate_data(
    cnt = 0
)

tb_substraction.add_with_substraction(
    cnt = 254
)

tb_predict.add_with_one_to_big(
    cnt = 254,
    substract=0, substract_mask=0x80
)
tb_predict.add_with_one_to_small(
    cnt = 254,
    substract=0x80, substract_mask=0x80
)

tb_forward.add_with_early_exit(
    exit_result=1,
    cnt=254,

    egress_spec = 1,
)

tb_forward.add_with_inference_routing(
    exit_result=0,
    cnt=254,

    egress_spec = 2,
)

for i in range(0,254):
    tb_forward.add_with_do_recirculation(
        exit_result=0,
        cnt=i
    )

#############################################################
################### Egress pipeline rules ###################
#############################################################

data_1 = 16
data_2 = 24
data_3_1 = 40
data_3_2 = 56
data_4_1 = 72
data_4_2 = 88
data_5 = 104
data_6 = 120
data_7 = 126

data_2_1 = 142
data_2_2 = 150
data_2_3_1 = 166
data_2_3_2 = 182
data_2_4_1 = 198
data_2_4_2 = 214
data_2_5 = 230
data_2_6 = 246
data_2_7 = 252

p4_egress = bfrt.tiniee_first.pipe.SwitchEgress

tb_exit_process = p4_egress.tb_exit_process

tb_activate_zero = p4_egress.tb_activate_zero

tb_activate_one = p4_egress.tb_activate_one

tb_invalid = p4_egress.tb_invalid

tb_exit_process.add_with_exit_process1(
    cnt = 253
)

tb_exit_process.add_with_exit_process2(
    cnt = 254
)

tb_invalid.add_with_invalid_header(
    cnt = 255,
    exit_result = 0
)

tb_invalid.add_with_early_exit(
    cnt = 255,
    exit_result = 1
)

for i in range(1,data_1+1):
    tb_activate_zero.add_with_activate_1_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_1_one(
        cnt = i
    )

for i in range(data_1+1,data_2+1):
    tb_activate_zero.add_with_activate_2_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_2_one(
        cnt = i
    )

for i in range(data_2+1,data_3_1+1):
    tb_activate_zero.add_with_activate_3_1_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_3_1_one(
        cnt = i
    )

for i in range(data_3_1+1,data_3_2+1):
    tb_activate_zero.add_with_activate_3_2_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_3_2_one(
        cnt = i
    )

for i in range(data_3_2+1,data_4_1+1):
    tb_activate_zero.add_with_activate_4_1_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_4_1_one(
        cnt = i
    )

for i in range(data_4_1+1,data_4_2+1):
    tb_activate_zero.add_with_activate_4_2_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_4_2_one(
        cnt = i
    )
for i in range(data_4_2+1,data_5+1):
    tb_activate_zero.add_with_activate_5_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_5_one(
        cnt = i
    )
for i in range(data_5+1,data_6+1):
    tb_activate_zero.add_with_activate_6_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_6_one(
        cnt = i
    )
for i in range(data_6+1,data_7+1):
    tb_activate_zero.add_with_activate_7_zero(
        cnt = i
    )
    tb_activate_one.add_with_activate_7_one(
        cnt = i
    )
for i in range(data_7+1,data_2_1+1):
    tb_activate_zero.add_with_activate_1_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_1_one_2(
        cnt = i
    )
for i in range(data_2_1+1,data_2_2+1):
    tb_activate_zero.add_with_activate_2_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_2_one_2(
        cnt = i
    )
for i in range(data_2_2+1,data_2_3_1+1):
    tb_activate_zero.add_with_activate_3_1_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_3_1_one_2(
        cnt = i
    )
for i in range(data_2_3_1+1,data_2_3_2+1):
    tb_activate_zero.add_with_activate_3_2_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_3_2_one_2(
        cnt = i
    )
for i in range(data_2_3_2+1,data_2_4_1+1):
    tb_activate_zero.add_with_activate_4_1_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_4_1_one_2(
        cnt = i
    )
for i in range(data_2_4_1+1,data_2_4_2+1):
    tb_activate_zero.add_with_activate_4_2_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_4_2_one_2(
        cnt = i
    )
for i in range(data_2_4_2+1,data_2_5+1):
    tb_activate_zero.add_with_activate_5_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_5_one_2(
        cnt = i
    )
for i in range(data_2_5+1,data_2_6+1):
    tb_activate_zero.add_with_activate_6_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_6_one_2(
        cnt = i
    )
for i in range(data_2_6+1,data_2_7+1):
    tb_activate_zero.add_with_activate_7_zero_2(
        cnt = i
    )
    tb_activate_one.add_with_activate_7_one_2(
        cnt = i
    )