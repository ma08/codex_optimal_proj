import math

def main():
    num_seg, g = map(int, input().split())
    seg_length = []
    seg_angle = []
    for i in range(num_seg):
        seg_length.append(int(input().split()[0]))
        seg_angle.append(int(input().split()[1]))

    for i in range(num_seg):
        v = 0
        for j in range(i, num_seg-1):
            v += math.sqrt(2*g*seg_length[j]/math.cos(math.radians(seg_angle[j])))
        print(v)

if __name__ == "__main__":
    main()
