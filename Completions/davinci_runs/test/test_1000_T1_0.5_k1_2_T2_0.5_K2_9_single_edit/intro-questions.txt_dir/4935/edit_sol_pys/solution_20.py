

import math

def main():
    input_line = input()
    input_line = input_line.split()
    num_seg = int(input_line[0])
    g = float(input_line[1])
    seg_lengths = [0] * num_seg
    seg_angles = [0] * num_seg
    for i in range(num_seg):
        input_line = input()
        input_line = input_line.split()
        seg_lengths[i] = int(input_line[0])
        seg_angles[i] = int(input_line[1])

    for i in range(num_seg):
        v = 0
        for j in range(i, num_seg):
            v += math.sqrt(2*g*seg_lengths[j]/math.cos(math.radians(seg_angles[j]))) * 1000
        print(round(v, 2))

if __name__ == "__main__":
    main()
