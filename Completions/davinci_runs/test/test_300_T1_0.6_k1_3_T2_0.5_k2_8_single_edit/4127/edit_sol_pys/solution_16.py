
import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip().split()
    print(int(float(line[0]) * float(line[1])))
