
import math

def main():
    input_line = input()
    input_line = input_line.split()
    num_seg = int(input_line[0])
    g = float(input_line[1])
    seg_lengths = []
    seg_angles = []
    for i in range(num_seg):
        input_line = input()
        input_line = input_line.split()
        seg_lengths.append(float(input_line[0]))
        seg_angles.append(float(input_line[1]))

    for i in range(num_seg):
        v = 0
        for j in range(i, num_seg):
            v += math.sqrt(2 * g * seg_lengths[j] / math.cos(math.radians(seg_angles[j]))) / 100
        print(v)

if __name__ == "__main__":
    main()
