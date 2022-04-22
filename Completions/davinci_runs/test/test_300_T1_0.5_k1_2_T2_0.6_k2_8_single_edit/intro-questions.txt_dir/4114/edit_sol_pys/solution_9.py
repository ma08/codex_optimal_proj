

import numpy as np
import sys

N = int(input())

x_y_h = np.empty((N, 3), dtype = int)

for i in range(N):
    x_y_h[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(i+1, N):
        if x_y_h[i][0] == x_y_h[j][0]:
            if x_y_h[i][1] == x_y_h[j][1]:
                if x_y_h[i][2] != x_y_h[j][2]:
                    print("No")
                    exit()
            else:
                C = (x_y_h[i][1] + x_y_h[j][1]) / 2
                H = x_y_h[i][2] + abs(x_y_h[i][1] - C)
                break

for i in range(N):
    if x_y_h[i][0] == x_y_h[j][0] and x_y_h[i][1] == C:
        if x_y_h[i][2] != H:
            print("No")
            exit()
    else:
        if x_y_h[i][2] != abs(x_y_h[j][0] - x_y_h[i][0]) + abs(C - x_y_h[i][1]) + H:
            print("No")
            exit()

print(x_y_h[j][0], C, H)
