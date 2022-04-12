

def is_possible(C_X, C_Y, H):
    for i in range(N):
        if x_y_h[i][0] == C_X and x_y_h[i][1] == C_Y:
            if x_y_h[i][2] != H:
                return False
        else:
            if x_y_h[i][2] != abs(C_X - x_y_h[i][0]) + abs(C_Y - x_y_h[i][1]) + H:
                return False
    return True

import sys

N = int(input())

x_y_h = []
for i in range(N):
    x_y_h.append(list(map(int, sys.stdin.readline().split())))

for i in range(101):
    for j in range(101):
        for k in range(101):
            if is_possible(i, j, k):
                print(i, j, k)
                exit()

print("No")
