

from __future__ import division, print_function
from sys import stdin
from math import pi

def main():
    lines = stdin.readlines()
    n, s = [int(x) for x in lines[0].split()]
    holes = []
    for i in range(1, n+1):
        holes.append([int(x) for x in lines[i].split()])
    holes.sort(key=lambda x: x[3])
    slice_size = 100000 / s
    for i in range(s):
        start = i * slice_size
        end = (i+1) * slice_size
        total_volume = (end - start) * 10000 * 10000
        for hole in holes:
            if hole[2] + hole[0] < start:
                continue
            elif hole[2] - hole[0] > end:
                break
            else:
                total_volume -= 4/3 * pi * hole[0]**3
        print(total_volume / 10000 / 10000 / 10000)

main()
