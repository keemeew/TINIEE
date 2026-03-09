# ./build_tofino.sh <abs_path>/program.p4 program

PROGRAM_PATH=$1
PROGRAM=$2

$SDE/install/bin/bf-p4c $PROGRAM_PATH -Xp4c="--disable-parse-depth-limit" -g

cp -f $PROGRAM.tofino/$PROGRAM.conf $SDE/install/share/p4/targets/tofino/$PROGRAM.conf

cp -rf /home/tofino/$PROGRAM.tofino $SDE_INSTALL/

rm -r /home/tofino/$PROGRAM.tofino
