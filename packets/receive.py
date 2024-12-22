from scapy.all import *
from scapy.all import PcapReader, sendp, Ether, IP, TCP
from time import sleep, strftime
from collections import Counter
import time
import threading
import csv
import argparse
import os

parser = argparse.ArgumentParser(description='receiver parser')
parser.add_argument('--host', help="source host", type=str, action="store", required=True)
parser.add_argument('--topo', help='evaluation topology', type=str, required=True)
args = parser.parse_args()

global host_list, source_ip, received_tos

source_ip = 0
host_list = []
received_tos = []
global counters
global count
counters = {
    'task1': {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0}
}
count = 0
def delete_dup(lst):
    global host_list
    unique_list = sorted(list(set(lst)))
    if len(unique_list) > 0:
        host_list.append(unique_list)

def binary_to_ip(binary_str):
    octets = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    ip_address = '.'.join(str(int(octet, 2)) for octet in octets)
    return ip_address
def compute_metrics(tp, tn, fp, fn):
    recall = tp / (tp + fn) if (tp + fn) else 0
    precision = tp / (tp + fp) if (tp + fp) else 0
    accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) else 0
    f1score = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0
    return recall, precision, accuracy, f1score

def parse_csv(file_path):
    global host_list
    hosts = {f'S{i}': [] for i in range(1, 15)}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            srchost = row['srchost']
            dsthost = row['dsthost']
            src_address = binary_to_ip(row['src_address'])
            dst_address = binary_to_ip(row['dst_address'])
            if srchost in hosts:
                hosts[srchost].append(src_address)
            if dsthost in hosts:
                hosts[dsthost].append(dst_address)
    
    for key, value in hosts.items():
        delete_dup(value)

def set_ip(host):
    global host_list, source_ip
    s = host.index('s')
    switch_id = host[1:s]
    host_id = host[(s+1):]
    host_list
    source_ip = host_list[int(switch_id)-1][int(host_id)-1]

def read_labels(file_path):
    full_data = []
    with open(file_path, 'r') as file:
        for line in file:
            full_data.append(line.strip())
    return full_data

def log_packet(flow_id, src_ip, dst_ip, sport, dport, proto, timestamp, pkt_length, event):
    flow_data_file = "/home/mncgpu4/INI_schemes/TINIEE/temp_result/flow_time.csv"
    with open(flow_data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([flow_id, src_ip, dst_ip, sport, dport, proto, timestamp, pkt_length, event])

def create_packet(pktlen, proto, src, dst, sport, dport, flg, label):
    
    tos = (int(label) << 6)
    timestamp = time.time()
    flow_id = f"{src}-{dst}-{sport}-{dport}-{proto}"
    
    log_packet(flow_id, src, dst, sport, dport, proto, timestamp, 'send')

    packet = Ether(src='ff:ff:ff:ff:ff:ff', dst='ff:ff:ff:ff:ff:ff', type=0x800) / IP(src=src, dst=dst, len=pktlen, proto=proto, tos=tos) / TCP(sport=sport, dport=dport, flags=flg)
    packet = packet / (b'\x00' * (pktlen - len(packet)))

    return packet

def gen_pkt(file_path, host_name):
    global host_list, iface, source_ip
    extract_value = read_labels(file_path)
    #extract_value = extract_value[964:966]
    labels = read_labels("/home/mncgpu4/INI_schemes/TINIEE/packets/y1_test.txt")
    labels = labels[:1000]
    #labels = labels[964:966]

    packets = []
    for i, value in enumerate(extract_value):
        pktlen = int(value[:16], 2)
        proto = int(value[16:24], 2)
        src = value[24:56]
        dst = value[56:88]
        sport = int(value[88:104], 2)
        dport = int(value[104:120], 2)
        flg = int(value[120:], 2)

        src_ip = binary_to_ip(src)
        dst_ip = binary_to_ip(dst)
        set_ip(host_name)

        if src_ip == source_ip:
            packet = create_packet(pktlen, proto, src_ip, dst_ip, sport, dport, flg, labels[i])
            packets.append(packet)
        else:
            continue

    return packets

def print_metrics(file):
    global counters
    global count
    tp1 = counters['task1']['TP']
    tn1 = counters['task1']['TN']
    fp1 = counters['task1']['FP']
    fn1 = counters['task1']['FN']
    recall1, precision1, accuracy1, f1score1 = compute_metrics(tp1, tn1, fp1, fn1)
    total_packets = count

    file.write(f"Total Packets for Host {args.host}: {count}\n")
    file.write(f"Task 1 - Total Packets: {total_packets}, Recall: {recall1}, Precision: {precision1}, Accuracy: {accuracy1}, F1 Score: {f1score1}\n")
    file.flush()
    

def receive_packet(interface, file):
    global host_list, iface
    
    #print(f"Sniffing on interface: {interface}")
    sniff(iface=interface, prn=lambda x: handle_pkt(x, file), timeout = 200)

def calculate_sleep_time(host_name):
    
    parts1 = host_name.split('h')[1]
    parts2 = parts1.split('s')
    multiplier1 = int(parts2[0])
    multiplier2 = int(parts2[1])
    
    
    #sleep_time = 2 * multiplier2 + 10 * multiplier1
    sleep_time = 2 * multiplier2 + 10 * multiplier1
    sleep_time = 0
    return sleep_time

def handle_pkt(pkt, file):
    #print(f"Receving time is: {time.time()}")
    global counters, count
    try:
        if IP in pkt:
            tos = pkt[IP].tos
            dst = pkt[IP].dst
            src = pkt[IP].src
            receive_time = time.time()
            flow_id = f"{src}-{dst}-{pkt[TCP].sport}-{pkt[TCP].dport}-{pkt[IP].proto}"
            plt_length = len(pkt)
            if dst == source_ip:
                log_packet(flow_id, src, dst, pkt[TCP].sport, pkt[TCP].dport, pkt[IP].proto, receive_time, plt_length, 'receive')

                file.write(f"tos: {tos} src: {src} dst: {dst}\n")
                file.flush()
                label1 = (tos >> 6) & 0x03
                prediction1 = (tos >> 2) & 0x03

                count += 1
                file.write(f"Packet - tos: {tos}, label1: {label1}, prediction1: {prediction1}, count: {count}\n")
                file.flush()

                if label1 == prediction1:
                    if label1 == 1:
                        counters['task1']['TP'] += 1
                    else:
                        counters['task1']['TN'] += 1
                else:
                    if label1 == 1:
                        counters['task1']['FN'] += 1
                    else:
                        counters['task1']['FP'] += 1
            else:
                file.write(f"Packet not for this host - dst: {dst}, source_ip: {source_ip}\n")
                file.flush()
        else:
            file.write(f"Non-IP Packet: {pkt.summary()}\n")
            file.flush()
    except Exception as e:
        file.write(f"Error handling packet: {e}\n")
        file.flush()

def send_packet():
    global iface
    file_path = "/home/mncgpu4/INI_schemes/TINIEE/packets/x_test.txt"
    host_name = args.host
    
    sleep_time = calculate_sleep_time(args.host)
    #print(f"Host: {args.host}, sleep time: {sleep_time}")
    sleep(sleep_time)
    #print("Ready to send! Time is ", time.time())
    
    packets = gen_pkt(file_path, host_name)
    #sleep(0.1)
    for pkt in packets:
        #sendp(pkt, iface=iface, verbose=False)
        sendp(pkt, inter=0.1, iface=iface, verbose=False)
        #sleep(0.01)

    

def main():
    global host_list, iface
    global counters
    
    bind_layers(Ether, IP)
    bind_layers(IP, TCP)
    
    result_dir = "/home/mncgpu4/INI_schemes/TINIEE/temp_result"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    file_name = os.path.join(result_dir, "test" + str(args.host) + ".txt")
    flow_data_file = os.path.join(result_dir, "flow_time.csv")
    if not os.path.exists(flow_data_file):
        with open(flow_data_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['flow_id', 'src_ip', 'dst_ip', 'sport', 'dport', 'proto', 'timestamp', 'pkt_length', 'event'])

    if args.topo == 'Italian':
        file_path_csv = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Host_information_Italian.csv"
    if args.topo == 'Japanese':
        file_path_csv = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Host_information_Japanese.csv"
    if args.topo == 'NSFNET':
        file_path_csv = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Host_information_NSFNET.csv"
    parse_csv(file_path_csv)
    set_ip(args.host)
    ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth' in i]
    iface = ifaces[0]
    
    with open(file_name, 'a') as log_file:
        receive_packet(iface, log_file)
      
        print_metrics(log_file)

if __name__ == '__main__':
    main()
