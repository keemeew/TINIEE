from scapy.all import *
from scapy.all import PcapReader, sendp, Ether, IP, TCP
from time import sleep
from collections import Counter
import time
import threading
import csv
import argparse

def receive_process():
    global iface_process
    sniff(iface=iface_process, prn = lambda x: handle_pkt_process(x))


INFER_LEN = 17 

def parse_ether(frame: bytes):
    if len(frame) < 14:
        return None
    dst = frame[0:6]
    src = frame[6:12]
    ethertype = struct.unpack("!H", frame[12:14])[0]
    off = 14

    if ethertype in (0x8100, 0x88A8):
        if len(frame) < 18:
            return None
        ethertype = struct.unpack("!H", frame[16:18])[0]
        off = 18

    return {"dst": dst, "src": src, "ethertype": ethertype, "l3_off": off}

def parse_ipv4(frame: bytes, off: int):
    if len(frame) < off + 20:
        return None

    vihl = frame[off]
    version = vihl >> 4
    ihl = (vihl & 0x0F) * 4
    if version != 4 or ihl < 20 or len(frame) < off + ihl:
        return None

    tos = frame[off + 1]
    dscp = tos >> 2
    ecn = tos & 0x03
    ip_id = struct.unpack("!H", frame[off + 4: off + 6])[0]
    return {"dscp": dscp, "ecn": ecn, "l4_off": off + ihl, "id": ip_id}

def parse_inference_layer(frame: bytes, off: int):
    if len(frame) < off + INFER_LEN:
        return None
    layer = frame[off] 
    return {"layer": layer, "next_off": off + INFER_LEN}

def handle_pkt_process(pkt):
    recv_time = time.monotonic_ns()
    frame = bytes(pkt)

    eth = parse_ether(frame)
    if not eth:
        return

    ethertype_hex = f"0x{eth['ethertype']:04x}"
    dst_dec = int.from_bytes(eth["dst"], byteorder="big", signed=False)
    src_dec = int.from_bytes(eth["src"], byteorder="big", signed=False)

    ip = parse_ipv4(frame, eth["l3_off"])
    if not ip:
        return

    inf = parse_inference_layer(frame, ip["l4_off"])
    if not inf:
        return


def main():
    global iface_process
    
    iface_process = 'veth4'

    receive_thread = threading.Thread(target=receive_process, args=())
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
    