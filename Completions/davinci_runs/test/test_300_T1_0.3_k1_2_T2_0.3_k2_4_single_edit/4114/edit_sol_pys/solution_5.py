

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

for cx in range(101):
    for cy in range(101):
        h = xyh[0][2] + abs(cx - xyh[0][0]) + abs(cy - xyh[0][1])
        if all(h - abs(cx - x[0]) - abs(cy - x[1]) == x[2] for x in xyh if x[2] != 0):
            print(cx, cy, h)
