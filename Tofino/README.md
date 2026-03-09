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
   ./build_tofino.sh [abs_path for the cloned directory]/TINIEE/tofino/p4src/tiniee_first.p4 tiniee_first
   ```
   
### Run switch model
   ```
   $SDE/run_tofino_model.sh -p tiniee_first
   ```
   
### Run switch driver
   ```
   $SDE/run_switchd.sh -p tiniee_first
   bfshell> bfrt_python [abs_path for the cloned directory]/tiniee/rule/bfrt_rule_tiniee_first.py
   ```
   
### Packet generation
   ```
   [Sender] python3 [abs_path for the cloned directory]/tiniee/tofino/packets/send.py
   [Receiver 1] python3 [abs_path for the cloned directory]/tiniee/tofino/packets/receive_process.py
   [Receiver 2] python3 [abs_path for the cloned directory]/tiniee/tofino/packets/receive_exit.py
   ```
