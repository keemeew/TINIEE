import csv
global s1, s2, s3, s4, s5, s6, s7, s8, s9, s10

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

def binary_to_ip(binary_str):
    octets = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    ip_address = '.'.join(str(int(octet, 2)) for octet in octets)

    return ip_address

def delete_dup(lst):
    unique_list = list(set(lst))
    return unique_list

def parse_csv(file_path):
    global s1, s2, s3, s4, s5, s6, s7, s8, s9, s10
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
                
    s1 = delete_dup(s1)
    s2 = delete_dup(s2)
    s3 = delete_dup(s3)
    s4 = delete_dup(s4)
    s5 = delete_dup(s5)
    s6 = delete_dup(s6)
    s7 = delete_dup(s7)
    s8 = delete_dup(s8)
    s9 = delete_dup(s9)
    s10 = delete_dup(s10)

if __name__ == '__main__':
    # CSV 파일 경로
    file_path = "/home/p4/TINIEE/Topology_solution/Host_information_Italian.csv"

    # CSV 파일 파싱
    parsed_data = parse_csv(file_path)

    print("s1 :", len(s1))
    print("s2 :", len(s2))
    print("s3 :", len(s3))
    print("s4 :", len(s4))
    print("s5 :", len(s5))
    print("s6 :", len(s6))
    print("s7 :", len(s7))
    print("s8 :", len(s8))
    print("s9 :", len(s9))
    print("s10 :", len(s10))
