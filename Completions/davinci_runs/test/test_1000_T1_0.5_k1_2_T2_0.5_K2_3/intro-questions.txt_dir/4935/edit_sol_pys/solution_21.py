import sys

import math

def main():
    input_line = sys.stdin.readline()
    input_line = input_line.split()
    num_segs = int(input_line[0])
    g = float(input_line[1])
    seg_lengths = []
    seg_angles = []
    for i in range(num_segs):
        input_line = sys.stdin.readline()
        input_line = input_line.split()
        seg_lengths.append(int(input_line[0]))
        seg_angles.append(int(input_line[1]))

    for i in range(num_segs):
        v = 0
        for j in range(i, num_segs):
            v += math.sqrt(2*g*seg_lengths[j]/math.cos(math.radians(seg_angles[j])))
        print(v)

if __name__ == "__main__":
    main()
