# Implementation of TINIEE on Tofino
This is the implementation of TINIEE on the Tofino hardware switch with P4 language.

## Execution Steps
Our code is available in SDE 9.13.3.

### Clone Repository
```bash
git clone https://github.com/keemeew/TINIEE
```

### Compile P4 program
   ```
   [First submodel] ./build_tofino.sh [abs_path for the cloned directory]/TINIEE/tofino/p4src/tiniee_first.p4 tiniee_first

   [Second submodel] ./build_tofino.sh [abs_path for the cloned directory]/TINIEE/tofino/p4src/tiniee_second.p4 tiniee_second

   [Third submodel] ./build_tofino.sh [abs_path for the cloned directory]/TINIEE/tofino/p4src/tiniee_third.p4 tiniee_third
   ```
   
### Run switch model
   ```
   $SDE/run_tofino_model.sh -p tiniee_first
   ```
   
### Run switch driver
  ```
   [First model]
   $SDE/run_switchd.sh -p tiniee_first
   bfshell> bfrt_python [abs_path for the cloned directory]/tiniee/rule/bfrt_rule_tiniee_first.py

   [Second model]
   $SDE/run_switchd.sh -p tiniee_second
   bfshell> bfrt_python [abs_path for the cloned directory]/tiniee/rule/bfrt_rule_tiniee_second.py

   [Third model]
   $SDE/run_switchd.sh -p tiniee_third
   bfshell> bfrt_python [abs_path for the cloned directory]/tiniee/rule/bfrt_rule_tiniee_third.py
   ```
   
### Packet generation
   ```
   [Sender] python3 [abs_path for the cloned directory]/tiniee/tofino/packets/send.py

   [Receiver 1] python3 [abs_path for the cloned directory]/tiniee/tofino/packets/receive_process.py
   
   [Receiver 2] python3 [abs_path for the cloned directory]/tiniee/tofino/packets/receive_exit.py
   ```
