import os
from collections import defaultdict
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--topo', help='evaluation topology', type=str, required=True)
parser.add_argument('--sol', help='Solution (e.g. TINIEE, DINC, RANDOM)', type=str, required=True)
parser.add_argument('--th', help='Confidence Threshold', type=str, required=True)
parser.parse_args()
def parse_log_line(line):
    parts = line.strip().split(',')
    return {
        'flow_id': parts[0],
        'source_ip': parts[1],
        'dest_ip': parts[2],
        'source_port': int(parts[3]),
        'dest_port': int(parts[4]),
        'protocol': int(parts[5]),
        'timestamp': float(parts[6]),
        'packet_size': int(parts[7]),
        'direction': parts[8]
    }

def add_packet_id(logs):
    packet_id_counter_send = defaultdict(int)
    packet_id_counter_receive = defaultdict(int)
    packet_size_sum = defaultdict(int)
    updated_logs = []

    for log in logs:
        flow_id = log['flow_id']
        direction = log['direction']

        if direction == 'send':
            pkt_length = log['packet_size']
            packet_size_sum[flow_id] += pkt_length
            packet_id_counter_send[flow_id] += 1
            log['packet_id'] = packet_id_counter_send[flow_id]
        elif direction == 'receive':
            packet_id_counter_receive[flow_id] += 1
            log['packet_id'] = packet_id_counter_receive[flow_id]

        updated_logs.append(log)

    return updated_logs, packet_size_sum

def calculate_packet_delays(logs):
    packet_times = defaultdict(lambda: {'send': {}, 'receive': {}})
    packet_delays = defaultdict(list)
    all_packet_delays = []

    for log in logs:
        flow_id = log['flow_id']
        timestamp = log['timestamp']
        direction = log['direction']
        packet_id = log['packet_id']

        packet_times[flow_id][direction][packet_id] = timestamp

    for flow_id, directions in packet_times.items():
        send_times = directions['send']
        receive_times = directions['receive']

        for packet_id in send_times.keys():
            if packet_id in receive_times:
                send_time = send_times[packet_id]
                receive_time = receive_times[packet_id]
                delay = receive_time - send_time
                packet_delays[flow_id].append((packet_id, delay))
                all_packet_delays.append(delay)

    return packet_delays, all_packet_delays

def calculate_average(values):
    total = sum(values)
    average = total / len(values) if values else 0
    return average

def parse_log_file(file_path):
    parsed_logs = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parsed_logs.append(parse_log_line(line))
    return parsed_logs

def process_single_log_file(file_path):
    parsed_logs = parse_log_file(file_path)
    updated_logs, packet_size_sum = add_packet_id(parsed_logs)
    return updated_logs, packet_size_sum

def write_results(packet_delays, average_packet_delay, packet_output_file):
    with open(packet_output_file, 'w') as file:
        for flow_id, delays in packet_delays.items():
            for packet_id, delay in delays:
                file.write(f"{flow_id},packet_id: {packet_id},delay: {delay}\n")
        file.write(f"Average Packet Delay,{average_packet_delay}\n")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.topo == 'Italian':
        topo = 'ita'
    if args.topo == 'Japanese':
        topo = 'jpn'
    if args.topo == 'NSFNET':
        topo = 'nsf'
    file_path = "/home/mncgpu4/INI_schemes/TINIEE/temp_result/flow_time.csv"
    if args.sol == 'NN':
        packet_delay_output_file = f"/home/mncgpu4/INI_schemes/TINIEE/result/{topo}/NNsplit/packet_delays.csv"
    else:
        packet_delay_output_file = f"/home/mncgpu4/INI_schemes/TINIEE/result/{topo}/{args.sol}/{args.th}/packet_delays.csv"
    #flow_completion_output_file = f"/home/mncgpu4/INI_schemes/TINIEE/temp_result/flow_completion_times.csv"
    #packet_delay_output_file = f"/home/mncgpu4/INI_schemes/TINIEE/temp_result/packet_delays.csv"
    parsed_logs, packet_size_sum = process_single_log_file(file_path)
    
    
    packet_delays, all_packet_delays = calculate_packet_delays(parsed_logs)
    
    average_packet_delay = calculate_average(all_packet_delays)
    
    write_results(packet_delays, average_packet_delay, packet_delay_output_file)
    
    print(f"Packet delays written to {packet_delay_output_file}")
