# coding: utf-8

import sys

N = int(input())

positions = []
for i in range(N):
    positions.append(list(map(int, sys.stdin.readline().split())))

for C_X in range(101):
    for C_Y in range(101):
        H = -1
        for position in positions:
            if H == -1:
                if position[2] != 0:
                    H = position[2] + abs(C_X - position[0]) + abs(C_Y - position[1])
            else:
                if position[2] != max(0, H - abs(C_X - position[0]) - abs(C_Y - position[1])):
                    break
        else:
            print(C_X, C_Y, H)
            exit()

for i in range(N):
    if x_y_h[i][0] == C_X and x_y_h[i][1] == C_Y:
        if x_y_h[i][2] != H:
            print("No")
            exit()
    else:
        if x_y_h[i][2] != abs(C_X - x_y_h[i][0]) + abs(C_Y - x_y_h[i][1]) + H:
            print("No")
            exit()

print(C_X, C_Y, H)
