

from __future__ import division
from sys import stdin
from math import pi

def main():
    lines = stdin.readlines()
    n = int(lines[0].split()[0])  # number of holes
    s = int(lines[0].split()[1])  # number of slices
    holes = []
    for i in range(1, n+1):
        line = lines[i].split()
        holes.append((int(line[0]), int(line[1]), int(line[2]), int(line[3])))  # r, x, y, z
    holes.sort(key=lambda x: x[3])
    slice_size = 1000000 / s  # 1 million / number of slices
    for i in range(s):
        start = i * slice_size
        end = (i+1) * slice_size
        total_volume = (end - start) * 10000 * 10000 * 10000  # 10 km cube
        for hole in holes:
            if hole[3] + hole[0] < start:
                continue
            elif hole[3] - hole[0] > end:
                break
            else:
                total_volume -= 4/3 * pi * hole[0] * hole[0] * hole[0]
        print(total_volume / 10000 / 10000 / 10000)  # print volume in km^3

main()
