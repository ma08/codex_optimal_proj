
import math

def main():
    lines = input()
    lines = lines.split()
    num_seg = int(lines[0])
    g = float(lines[1])
    seg_length = []
    seg_angle = []
    for i in range(num_seg):
        lines = input()
        lines = lines.split()
        seg_length.append(int(lines[0]))
        seg_angle.append(int(lines[1]))

    for i in range(num_seg):
        v = 0
        for j in range(i, num_seg):
            v += math.sqrt(2*g*seg_length[j]/math.cos(math.radians(seg_angle[j])))/2
        print(v)

if __name__ == "__main__":
    main()
