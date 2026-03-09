from scapy.all import *
from scapy.all import PcapReader, sendp, Ether, IP, TCP
from time import sleep
from collections import Counter
import time
import threading
import csv
import argparse
import struct

iface_exit = "veth2"
TYPE_EXIT = 0x8890 


def receive_exit():
    global iface_exit
    sniff(iface=iface_exit, prn = lambda x: handle_pkt_exit(x))

TYPE_EXIT = 0x8890 

def mac_str(b: bytes) -> str:
    return ":".join(f"{x:02x}" for x in b)

def ipv4_str(b: bytes) -> str:
    return socket.inet_ntoa(b)

def parse_ether_and_ipv4(frame: bytes):
    if len(frame) < 14:
        return None

    dst = frame[0:6]
    src = frame[6:12]
    ethertype = struct.unpack("!H", frame[12:14])[0]
    l3_off = 14

    if ethertype in (0x8100, 0x88A8) and len(frame) >= 18:
        ethertype = struct.unpack("!H", frame[16:18])[0]
        l3_off = 18

    return (dst, src, ethertype, l3_off)

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

def handle_pkt_exit(pkt):
    recv_time = time.monotonic_ns()
    frame = bytes(pkt)
    parsed = parse_ether_and_ipv4(frame)
    if not parsed:
        return

    dst, src, ethertype, l3_off = parsed

    dst_dec = int.from_bytes(dst, byteorder="big", signed=False)
    src_dec = int.from_bytes(src, byteorder="big", signed=False)

    if ethertype != TYPE_EXIT:
        return

    ip = parse_ipv4(frame, l3_off)
    if ip is None:
        return

def main():
    global iface_exit
    
    iface_exit = 'veth2'
    
    receive_thread = threading.Thread(target=receive_exit, args=())
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
    