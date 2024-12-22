import os
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--topo', help='evaluation topology', type=str, required=True)
parser.add_argument('--sol', help='Solution (e.g. TINIEE, DINC)', type=str, required=True)
parser.add_argument('--th', help='Confidence Threshold', type=str, required=True)
parser.parse_args()
def parse_host_file(file_path):
    tp, tn, fp, fn = 0, 0, 0, 0
    count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            if 'Packet - tos' in line:
                label1 = int(re.search(r'label1: (\d+)', line).group(1))
                prediction1 = int(re.search(r'prediction1: (\d+)', line).group(1))
                count += 1
                if label1 == prediction1:
                    if label1 == 1:
                        tp += 1
                    else:
                        tn += 1
                else:
                    if label1 == 1:
                        fn += 1
                    else:
                        fp += 1
    return tp, tn, fp, fn, count

def compute_metrics(tp, tn, fp, fn):
    recall = tp / (tp + fn) if (tp + fn) else 0
    precision = tp / (tp + fp) if (tp + fp) else 0
    accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) else 0
    f1score = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0
    return recall, precision, accuracy, f1score

def aggregate_metrics(directory):
    total_tp, total_tn, total_fp, total_fn, total_count = 0, 0, 0, 0, 0
    for filename in os.listdir(directory):
        if filename.startswith('test') and filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            tp, tn, fp, fn, count = parse_host_file(file_path)
            total_tp += tp
            total_tn += tn
            total_fp += fp
            total_fn += fn
            total_count += count

    recall, precision, accuracy, f1score = compute_metrics(total_tp, total_tn, total_fp, total_fn)
    result = {
        'total_packets': total_count,
        'recall': recall,
        'precision': precision,
        'accuracy': accuracy,
        'f1score': f1score
    }
    return result

def write_aggregated_metrics(result, result_file):
    with open(result_file, 'w') as file:
        file.write(f"Total Packets: {result['total_packets']}\n")
        file.write(f"Recall: {result['recall']}\n")
        file.write(f"Precision: {result['precision']}\n")
        file.write(f"Accuracy: {result['accuracy']}\n")
        file.write(f"F1 Score: {result['f1score']}\n")

if __name__ == '__main__':
    args = parser.parse_args()
    
    # Determine topology abbreviation
    if args.topo == 'Italian':
        topo = 'ita'
    elif args.topo == 'Japanese':
        topo = 'jpn'
    elif args.topo == 'NSFNET':
        topo = 'nsf'

    # Determine result file path
    directory = "/home/mncgpu4/INI_schemes/TINIEE/temp_result"
    if args.sol == 'NN':
        result_file = f"/home/mncgpu4/INI_schemes/TINIEE/result/{topo}/NNsplit/accuracy_result.txt"
    else:
        result_file = f"/home/mncgpu4/INI_schemes/TINIEE/result/{topo}/{args.sol}/{args.th}/accuracy_result.txt"

    # Aggregate metrics and write to the result file
    aggregated_metrics = aggregate_metrics(directory)
    write_aggregated_metrics(aggregated_metrics, result_file)
    
    print(f"Aggregated metrics written to {result_file}")
