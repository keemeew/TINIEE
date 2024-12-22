import argparse
from p4utils.mininetlib.network_API import NetworkAPI
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.link import TCLink
import ast
from multiprocessing import Process
import threading
import time
import subprocess
import pandas as pd
import sys
sys.path.append('/home/mncgpu4/.local/lib/python3.8/site-packages')
from time import sleep, strftime
import csv
global host_list
import os


host_list= []

def binary_to_ip(binary_str):
    octets = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    ip_address = '.'.join(str(int(octet, 2)) for octet in octets)
    return ip_address

def delete_dup(lst):
    global host_list
    unique_list = sorted(list(set(lst)))
    if len(unique_list) > 0:
        host_list.append(unique_list)

def get_switch_commands(cs_value, solution, filename):
    # Load the CSV data from the file
    df = pd.read_csv(filename)
    
    cs_value = float(cs_value)
    
    if cs_value == 0.95:
        cs_value = 0.9
    # Filter data for the given CS value
    
    row = df[df['CS'] == cs_value]

    
    if row.empty:
        raise ValueError(f"No data found for CS value {cs_value}")
    if solution == 'NN':
        solution = 'DINC'
    # Get the solution list
    solution_str = row[f'{solution}_sol'].values[0]
    solution_list = ast.literal_eval(solution_str)
    
    return solution_list
def parse_csv(file_path):
    global host_list
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []
    s6 = []
    s7 = []
    s8 = []
    s9 = []
    s10 = []
    s11 = []
    s12 = []
    s13 = []
    s14 = []
    s15 = []
    s16 = []
    s17 = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            srchost = row['srchost']
            dsthost = row['dsthost']
            src_address = row['src_address']
            src_address = binary_to_ip(src_address)
            dst_address = row['dst_address']
            dst_address = binary_to_ip(dst_address)
            if srchost == 'S1':
                s1.append(src_address)
            if dsthost == 'S1':
                s1.append(dst_address)
            if srchost == 'S2':
                s2.append(src_address)
            if dsthost == 'S2':
                s2.append(dst_address)
            if srchost == 'S3':
                s3.append(src_address)
            if dsthost == 'S3':
                s3.append(dst_address)
            if srchost == 'S4':
                s4.append(src_address)
            if dsthost == 'S4':
                s4.append(dst_address)
            if srchost == 'S5':
                s5.append(src_address)
            if dsthost == 'S5':
                s5.append(dst_address)
            if srchost == 'S6':
                s6.append(src_address)
            if dsthost == 'S6':
                s6.append(dst_address)
            if srchost == 'S7':
                s7.append(src_address)
            if dsthost == 'S7':
                s7.append(dst_address)
            if srchost == 'S8':
                s8.append(src_address)
            if dsthost == 'S8':
                s8.append(dst_address)
            if srchost == 'S9':
                s9.append(src_address)
            if dsthost == 'S9':
                s9.append(dst_address)
            if srchost == 'S10':
                s10.append(src_address)
            if dsthost == 'S10':
                s10.append(dst_address)
            if srchost == 'S11':
                s11.append(src_address)
            if dsthost == 'S11':
                s11.append(dst_address)
            if srchost == 'S12':
                s12.append(src_address)
            if dsthost == 'S12':
                s12.append(dst_address)
            if srchost == 'S13':
                s13.append(src_address)
            if dsthost == 'S13':
                s13.append(dst_address)
            if srchost == 'S14':
                s14.append(src_address)
            if dsthost == 'S14':
                s14.append(dst_address)
            if srchost == 'S15':
                s15.append(src_address)
            if dsthost == 'S15':
                s15.append(dst_address)
            if srchost == 'S16':
                s16.append(src_address)
            if dsthost == 'S16':
                s16.append(dst_address)
            if srchost == 'S17':
                s17.append(src_address)
            if dsthost == 'S17':
                s17.append(dst_address)
    delete_dup(s1)
    delete_dup(s2)
    delete_dup(s3)
    delete_dup(s4)
    delete_dup(s5)
    delete_dup(s6)
    delete_dup(s7)
    delete_dup(s8)
    delete_dup(s9)
    delete_dup(s10)
    delete_dup(s11)
    delete_dup(s12)
    delete_dup(s13)
    delete_dup(s14)
    delete_dup(s15)
    delete_dup(s16)
    delete_dup(s17)
    for lst in host_list:
        print(lst)
    
# # Run command on Mininet node
def run_command_on_host(host, command):
    #result = host_node.cmd(command)
    subprocess.run(['mnexec', '-a', str(host.pid), 'sh', '-c', command], check=True) #수정함
    # print(f"Command result on {host_node.name}:\n{result}")
# Configure Network
def config_network(p4_ee_1, p4_ee_2, p4_ee_3, p4_nf, topo, sol, switch_sol):
    global host_list
  
    net = NetworkAPI()
    
    # If want to use Mininet CLI, modify to True
    net.cli_enabled = False

    hosts = []
    for i in range(len(host_list)):
        for j in range(len(host_list[i])):
            hosts.append(net.addHost(f'h{i+1}s{j+1}'))
   
    
    # Network general options
    net.setLogLevel('info')
    #net.setLogLevel('debug')
      
    def add_p4_switch_with_log(switch_name, p4_source, cli_input=None):
        log_dir = '/home/mncgpu4/INI_schemes/TINIEE/'
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, f'p4s.{switch_name}.log')
        pid_file = os.path.join(log_dir, f'p4s.{switch_name}.pid')
        switch = net.addP4Switch(switch_name, log_file=log_file, pid_file=pid_file, cli_input=cli_input)
        net.setP4Source(switch_name, p4_source)
        return switch


    if topo == "Italian":

        linkops = dict(bw=1000, delay='1ms', loss=0, use_htb=True) 
        linkops2 = dict(bw=1000, delay='70ms', loss=0, use_htb=True)
        linkops3 = dict(bw=1000, delay='84ms', loss=0, use_htb=True)
        linkops4 = dict(bw=1000, delay='105ms', loss=0, use_htb=True)
        linkops1 = dict(bw=1000, delay='63ms', loss=0, use_htb=True) 
        linkops5 = dict(bw=1000, delay='119ms', loss=0, use_htb=True)
        linkops6 = dict(bw=1000, delay='126ms', loss=0, use_htb=True)
        linkops7 = dict(bw=1000, delay='140ms', loss=0, use_htb=True)
        linkops8 = dict(bw=1000, delay='147ms', loss=0, use_htb=True)
        linkops9 = dict(bw=1000, delay='189ms', loss=0, use_htb=True)
        linkops10 = dict(bw=1000, delay='217ms', loss=0, use_htb=True)
        linkops11 = dict(bw=1000, delay='245ms', loss=0, use_htb=True)
        linkops12 = dict(bw=1000, delay='210ms', loss=0, use_htb=True)



        if sol == "TINIEE":
            # Add Early Exit switch with rules
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/TINIEE/S{sol_1}_command_routing_ita_TINIEE_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/TINIEE/S{sol_2}_command_routing_ita_TINIEE_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/TINIEE/S{sol_3}_command_routing_ita_TINIEE_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/TINIEE/S{non_sol_1}_command_routing_ita_TINIEE_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)
        if sol == "DINC":
            # Add Early Exit switch with rules
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/DINC/S{sol_1}_command_routing_ita_DINC_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/DINC/S{sol_2}_command_routing_ita_DINC_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/DINC/S{sol_3}_command_routing_ita_DINC_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/DINC/S{non_sol_1}_command_routing_ita_DINC_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)

        if sol == "NN":
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/NN/S{sol_1}_command_routing_ita_NN_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/NN/S{sol_2}_command_routing_ita_NN_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/NN/S{sol_3}_command_routing_ita_NN_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Italian/NN/S{non_sol_1}_command_routing_ita_NN_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)



        # Construct Network Topology
        #print(host_list)

        ### Host - switch
        for i in range(len(host_list)):
            for j in range(len(host_list[i])):
                net.addLink(f'h{i+1}s{j+1}', f's{i+1}',**linkops)
    

        ### Switch - Switch
        net.addLink('s1', 's2',**linkops12)
        net.addLink('s1', 's3',**linkops12)

        net.addLink('s2', 's4',**linkops3)
        net.addLink('s2', 's6',**linkops6)

        net.addLink('s3', 's6',**linkops10)
        net.addLink('s3', 's7',**linkops4)

        net.addLink('s4', 's5',**linkops5)

        net.addLink('s5', 's6',**linkops7)
        net.addLink('s5', 's10',**linkops9)

        net.addLink('s6', 's7',**linkops11)
        net.addLink('s6', 's9',**linkops1)
        net.addLink('s6', 's10',**linkops8)

        net.addLink('s7', 's8',**linkops8)

        net.addLink('s8', 's9',**linkops7)

        net.addLink('s9', 's10',**linkops2)
    
    if topo == "Japanese":
        # Link option
        linkops = dict(bw=1000, delay='1ms', loss=0, use_htb=True) # for host - switch
        linkops1 = dict(bw=1000, delay='20ms', loss=0, use_htb=True) 
        linkops2 = dict(bw=1000, delay='40ms', loss=0, use_htb=True)
        linkops3 = dict(bw=1000, delay='80ms', loss=0, use_htb=True)
        linkops4 = dict(bw=1000, delay='120ms', loss=0, use_htb=True)
        linkops5 = dict(bw=1000, delay='160ms', loss=0, use_htb=True)
        if sol == "TINIEE":
            # Add Early Exit switch with rules
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/TINIEE/S{sol_1}_command_routing_jpn_TINIEE_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/TINIEE/S{sol_2}_command_routing_jpn_TINIEE_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/TINIEE/S{sol_3}_command_routing_jpn_TINIEE_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/TINIEE/S{non_sol_1}_command_routing_jpn_TINIEE_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)
        if sol == "DINC":
            # Add Early Exit switch with rules
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/DINC/S{sol_1}_command_routing_jpn_DINC_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/DINC/S{sol_2}_command_routing_jpn_DINC_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/DINC/S{sol_3}_command_routing_jpn_DINC_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/DINC/S{non_sol_1}_command_routing_jpn_DINC_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)

        if sol == "NN":
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/NN/S{sol_1}_command_routing_jpn_NN_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/NN/S{sol_2}_command_routing_jpn_NN_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/NN/S{sol_3}_command_routing_jpn_NN_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/Japanese/NN/S{non_sol_1}_command_routing_jpn_NN_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)
            

        # Construct Network Topology

        ### Host - switch
        for i in range(len(host_list)):
            for j in range(len(host_list[i])):
                net.addLink(f'h{i+1}s{j+1}', f's{i+1}',**linkops)
 
        ### Switch - Switch
        net.addLink('s1', 's2',**linkops3)
        net.addLink('s1', 's3',**linkops4)

        net.addLink('s2', 's4',**linkops4)

        net.addLink('s3', 's5',**linkops4)

        net.addLink('s4', 's5',**linkops2)
        net.addLink('s4', 's6',**linkops1)

        net.addLink('s5', 's6',**linkops1)
        net.addLink('s5', 's7',**linkops2)
        net.addLink('s5', 's9',**linkops4)

        net.addLink('s6', 's8',**linkops3)

        net.addLink('s7', 's8',**linkops2)
        net.addLink('s7', 's12',**linkops4)

        net.addLink('s8', 's10',**linkops3)

        net.addLink('s9', 's12',**linkops4)
        net.addLink('s9', 's14',**linkops4)

        net.addLink('s10', 's11',**linkops1)
        net.addLink('s10', 's12',**linkops1)

        net.addLink('s11', 's12',**linkops1)
        net.addLink('s11', 's13',**linkops5)

        net.addLink('s12', 's13',**linkops5)
        net.addLink('s12', 's14',**linkops4)

        net.addLink('s13', 's14',**linkops3)
    
    if topo == "NSFNET":
        # Link option
        linkops = dict(bw=1000, delay='1ms', loss=0, use_htb=True) # for host - switch
        linkops1 = dict(bw=1000, delay='30ms', loss=0, use_htb=True) 
        #linkops2 = dict(bw=1000, delay='0.4ms', loss=0, use_htb=True) 
        linkops2 = dict(bw=1000, delay='50ms', loss=0, use_htb=True) 
        linkops3 = dict(bw=1000, delay='60ms', loss=0, use_htb=True) 
        linkops4 = dict(bw=1000, delay='70ms', loss=0, use_htb=True) 
        linkops5 = dict(bw=1000, delay='80ms', loss=0, use_htb=True) 
        linkops6 = dict(bw=1000, delay='90ms', loss=0, use_htb=True) 
        linkops7 = dict(bw=1000, delay='110ms', loss=0, use_htb=True) 
        linkops8 = dict(bw=1000, delay='120ms', loss=0, use_htb=True) 
        linkops9 = dict(bw=1000, delay='160ms', loss=0, use_htb=True) 
        linkops10 = dict(bw=1000, delay='200ms', loss=0, use_htb=True) 
        linkops11 = dict(bw=1000, delay='240ms', loss=0, use_htb=True) 
        linkops12 = dict(bw=1000, delay='280ms', loss=0, use_htb=True) 
        
        
        if sol == "TINIEE":
            # Add Early Exit switch with rules
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/TINIEE/S{sol_1}_command_routing_NSFNET_TINIEE_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/TINIEE/S{sol_2}_command_routing_NSFNET_TINIEE_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/TINIEE/S{sol_3}_command_routing_NSFNET_TINIEE_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/TINIEE/S{non_sol_1}_command_routing_NSFNET_TINIEE_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)

        if sol == "DINC":
            # Add Early Exit switch with rules
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/DINC/S{sol_1}_command_routing_NSFNET_DINC_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/DINC/S{sol_2}_command_routing_NSFNET_DINC_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/DINC/S{sol_3}_command_routing_NSFNET_DINC_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/DINC/S{non_sol_1}_command_routing_NSFNET_DINC_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)

        if sol == "NN":
            switch_sol = [s.replace('S', 's') for s in switch_sol]
            sol_sw = switch_sol
            sw = ['s1','s2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14']
            sw = list(set(sw)-set(sol_sw))
     
            sol_1 = sol_sw[0].split('s')[1]
       
            sol_2 = sol_sw[1].split('s')[1]
            sol_3 = sol_sw[2].split('s')[1]
            non_sol = [i for i in sw]
            net.addP4Switch(sol_sw[0],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/NN/S{sol_1}_command_routing_NSFNET_NN_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[1],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/NN/S{sol_2}_command_routing_NSFNET_NN_new.txt', log_enabled=True)
            net.addP4Switch(sol_sw[2],cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/NN/S{sol_3}_command_routing_NSFNET_NN_new.txt', log_enabled=True)
            ### Add Early Exit switch P4 code
            net.setP4Source(sol_sw[0],p4_ee_1)
            net.setP4Source(sol_sw[1],p4_ee_2)
            net.setP4Source(sol_sw[2],p4_ee_3)
            for i in non_sol:
                non_sol_1 = i.split('s')[1]
                net.addP4Switch(f'{i}',cli_input= f'/home/mncgpu4/INI_schemes/TINIEE/rule/NSFNET/NN/S{non_sol_1}_command_routing_NSFNET_NN_new.txt', log_enabled=True)
                net.setP4Source(f'{i}',p4_nf)


        ### Host - switch
        for i in range(len(host_list)):
            for j in range(len(host_list[i])):
                net.addLink(f'h{i+1}s{j+1}', f's{i+1}',**linkops)
   
        ### Switch - Switch
        net.addLink('s1', 's2',**linkops7)
        net.addLink('s1', 's3',**linkops9)
        net.addLink('s1', 's8',**linkops12)

        net.addLink('s2', 's3',**linkops3)
        net.addLink('s2', 's4',**linkops)

        net.addLink('s3', 's6',**linkops10)

        net.addLink('s4', 's5',**linkops3)
        net.addLink('s4', 's11',**linkops11)

        net.addLink('s5', 's6',**linkops7)
        net.addLink('s5', 's7',**linkops5)

        net.addLink('s6', 's10',**linkops8)
        net.addLink('s6', 's13',**linkops10)

        net.addLink('s7', 's8',**linkops4)

        # net.addLink('s8', 's8',**linkops13)
        net.addLink('s8', 's9',**linkops4)
        
        net.addLink('s9', 's10',**linkops6)
        net.addLink('s9', 's12',**linkops2)
        net.addLink('s9', 's14',**linkops2)

        net.addLink('s11', 's12',**linkops5)
        net.addLink('s11', 's14',**linkops5)
        
        

        net.addLink('s12', 's13',**linkops1)

        net.addLink('s13', 's14',**linkops1)

    # Assignment strategy
    net.mixed()

    # Nodes general options: Log, Pcap ,,,
    net.enableCpuPortAll()
    net.enablePcapDumpAll()
    net.enableLogAll()

    return net, sol_sw

# Parser for P4 program and number of sending packets
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--p4_ee_1', help='Early Exit first layer p4 src file.', type=str, required=True)
    parser.add_argument('--p4_ee_2', help='Early Exit second layer p4 src file.', type=str, required=True)
    parser.add_argument('--p4_ee_3', help='Early Exit third layer p4 src file.', type=str, required=True)
    parser.add_argument('--p4_nf', help='Normal Forwarding p4 src file.', type=str, required=True)
    parser.add_argument('--topo', help='evaluation topology', type=str, required=True)
    parser.add_argument('--sol', help='Solution (e.g. TINIEE, DINC, RANDOM)', type=str, required=True)
    parser.add_argument('--th', help='Confidence Threshold', type=str, required=True)
    # parser.add_argument('--cs', help='Confidence Score threshold', type=int, required=True)
    return parser.parse_args()
def get_switch_stats(net, log_file):
    switches = net.switches
    with open(log_file, 'a') as f:
        for switch in switches:
            cmd = "ovs-ofctl dump-ports {}".format(switch.name)
            result = switch.cmd(cmd)
            timestamp = strftime("%Y-%m-%d %H:%M:%S")
            f.write("Timestamp: {}\n".format(timestamp))
            f.write("Stats for switch {}:\n{}\n".format(switch.name, result))

def get_host_packet_stats(net, log_file):
    hosts = net.hosts
    with open(log_file, 'a') as f:
        for host in hosts:
            cmd = "ifconfig"
            result = host.cmd(cmd)
            timestamp = strftime("%Y-%m-%d %H:%M:%S")
            f.write("Timestamp: {}\n".format(timestamp))
            f.write("Stats for host {}:\n{}\n".format(host.name, result))
def get_exithost_interfaces(net, host_name):
    exithost = net.net.get(host_name)
    interfaces = exithost.cmd('ifconfig -a')
    return interfaces


def update_rules(rule_path, threshold):
    with open(rule_path, 'r') as file:
        lines = file.readlines()

    with open(rule_path, 'w') as file:
        for line in lines:
            if "threshold" in line:
                file.write(f"set threshold {threshold}\n")
            else:
                file.write(line)

def main():
    global host_list
    args = get_args()
    

    # Read the flow information and host lists
    if args.topo == "Italian" or args.topo == "Linear":
        file_path = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Host_information_Italian.csv"
        sol_path = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Solution_Italian.csv"
    if args.topo == "Japanese":
        file_path = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Host_information_Japanese.csv"
        sol_path = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Solution_Japanese.csv"
    if args.topo == "NSFNET":
        file_path = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Host_information_NSFNET.csv"
        sol_path = "/home/mncgpu4/INI_schemes/TINIEE/Topology_solution/Solution_NSFNET.csv"
    parsed_data = parse_csv(file_path)
    
    switch_sol = get_switch_commands(args.th, args.sol, sol_path)
    # Config and start the networks
    
    net, sol_sw = config_network(args.p4_ee_1, args.p4_ee_2, args.p4_ee_3, args.p4_nf, args.topo, args.sol, switch_sol)
    # net = config_network(args.p4_ee_1, args.p4_ee_2, args.p4_ee_3, args.p4_nf, args.topo, args.sol, args.cs)
    net.startNetwork()

   

    # # Execute command on Mininet nodes simultaneously
    commands = []
    receive_processes = []
    send_processes = []
    receive_commands = []
    send_commands = []
    send_command = []
    receive_command = []
    send_threads = []
    receive_threads = []

    count = 0

    for i in range(len(host_list)):
        for j in range(len(host_list[i])):
            
            receive_command = f'python3 /home/mncgpu4/INI_schemes/TINIEE/packets/receive.py --host "h{i+1}s{j+1}" --topo {args.topo}'
            send_command = f'python3 /home/mncgpu4/INI_schemes/TINIEE/packets/send.py --host "h{i+1}s{j+1}" --topo {args.topo}'
            receive_commands.append(receive_command)
            send_commands.append(send_command)
    for i in range(len(host_list)):
        for j in range(len(host_list[i])):
            host = net.net.get(f'h{i+1}s{j+1}')
            #receive_process = Process(target=run_command_on_host, args=(net.net.get(f'h{i+1}s{j+1}'), receive_commands[count]))
            receive_process = threading.Thread(target=run_command_on_host, args=(host, receive_commands[count]))
            
            #print(f'h{i+1}s{j+1}')
            count += 1
            receive_process.start()
            
            receive_processes.append(receive_process)
    count = 0
    for i in range(len(host_list)):
        for j in range(len(host_list[i])):
            host = net.net.get(f'h{i+1}s{j+1}')
            
            # send_process = Process(target=run_command_on_host, args=(net.net.get(f'h{i+1}s{j+1}'), send_commands[count]))
            send_process = threading.Thread(target=run_command_on_host, args=(host, send_commands[count]))
            
            #print(f'h{i+1}s{j+1}')
            
            count += 1
            
            send_process.start()
            send_processes.append(send_process)
            
            

    
    for process in send_processes:
        print('process.join')
        process.join()
    for process in receive_processes:
        print('process.join')
        process.join()
    for thread in send_threads:
        thread.join()

    for thread in receive_threads:
        thread.join()
    

    # # # Turn off the Mininet
    os.system(f'python3 /home/mncgpu4/INI_schemes/TINIEE/packets/compute_result.py --topo {args.topo} --sol {args.sol} --th {args.th}')
    print(f'python3 /home/mncgpu4/INI_schemes/TINIEE/packets/compute_result.py --topo {args.topo} --sol {args.sol} --th {args.th}')
    os.system(f'python3 /home/mncgpu4/INI_schemes/TINIEE/packets/compute_delay.py --topo {args.topo} --sol {args.sol} --th {args.th}')
    print(f'python3 /home/mncgpu4/INI_schemes/TINIEE/packets/compute_delay.py --topo {args.topo} --sol {args.sol} --th {args.th}')
    
    net.stopNetwork()


if __name__ == '__main__':
    main()
