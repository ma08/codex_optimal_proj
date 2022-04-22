

import copy
import sys

N = int(input())

xyh = []
for i in range(N):
    xyh.append(list(map(int, sys.stdin.readline().split())))

# print(xyh)

for i in range(N):
    for j in range(i+1, N):
        if xyh[i][0] == xyh[j][0]:
            if xyh[i][1] == xyh[j][1]:
                if xyh[i][2] != xyh[j][2]:
                    print("No")
                    exit()
            else:
                C_X = xyh[i][0]
                C_Y = (xyh[i][1] + xyh[j][1]) / 2
                if xyh[i][2] == xyh[j][2]:
                    H = abs(xyh[i][1] - xyh[j][1]) + xyh[i][2]
                else:
                    H = abs(xyh[i][1] - xyh[j][1]) + max(xyh[i][2], xyh[j][2])
                break

for i in range(N):
    if xyh[i][0] == C_X and xyh[i][1] == C_Y:
        if xyh[i][2] != H:
            print("No")
            exit()

for i in range(N):
    if xyh[i][2] != abs(C_X - xyh[i][0]) + abs(C_Y - xyh[i][1]) + H:
        print("No")
        exit()

print(C_X, C_Y, H, sep=" ")
