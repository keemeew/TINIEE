from scapy.all import *
from scapy.all import PcapReader, sendp, Ether, IP, TCP
from time import sleep
from collections import Counter
import time
import threading
import csv
import argparse

def binary_to_ip(binary_str):
    octets = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    ip_address = '.'.join(str(int(octet, 2)) for octet in octets)
    return ip_address

def read_labels(file_path):
    full_data = []
    with open(file_path, 'r') as file:
        for line in file:
            full_data.append(line.strip())
    return full_data

def create_packet(pktlen,proto,src,dst,sport,dport,flg,idx):
    packet = Ether(src='ff:ff:ff:ff:ff:ff', dst='ff:ff:ff:ff:ff:ff') / IP(src=src, dst=dst, len = pktlen, proto=proto,id=idx)
    packet = packet / TCP (sport = sport, dport = dport, flags = flg) 
    packet = packet / (b'\x00' * (pktlen - 54))
    return packet

def gen_pkt(file_path):
    global host_list, iface
    global source_ip
    extract_value = read_labels(file_path)
    packets = []
    for i, value in enumerate(extract_value):
        pktlen = int(value[:16],2)
        proto = int(value[16:24],2)
        src = (value[24:56])
        dst = (value[56:88])
        sport = int(value[88:104],2)
        dport = int(value[104:120],2)
        flg = int(value[120:],2)

        src_ip = binary_to_ip(src)
        dst_ip = binary_to_ip(dst)

        packets.append(create_packet(pktlen,proto,src_ip,dst_ip,sport,dport,flg,i))
    return packets

def main():
    global iface_send
    
    iface_send = 'veth0'
        
    file_path = "~/tiniee/packets/x_test.txt"
    packets = gen_pkt(file_path)
    
    for i, packet in enumerate(packets):
        sleep(20)
        print(f"{i} {time.monotonic_ns()}")
        sendp(packet, iface = iface_send, verbose=False)

if __name__ == '__main__':
    main()
    