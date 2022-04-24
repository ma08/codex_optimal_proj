

import argparse

parser = argparse.ArgumentParser(description='File processing')
parser.add_argument('-f', '--file', help='file name', required=True)
args = parser.parse_args()

with open(args.file) as f:
    lines = f.readlines()

for line in lines:
    print(line.split())
