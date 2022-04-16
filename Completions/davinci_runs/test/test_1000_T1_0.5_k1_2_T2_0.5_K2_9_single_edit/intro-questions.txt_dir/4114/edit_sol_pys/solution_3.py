
import sys

N = int(input())

x_y_h = []
for i in range(N):
    x_y_h.append(list(map(int, sys.stdin.readline().split())))

for C_X in range(101):
    for C_Y in range(101):
        for H in range(101):
            for i in range(N):
                if x_y_h[i][0] == C_X and x_y_h[i][1] == C_Y:
                    if x_y_h[i][2] != H:
                        break
                else:
                    if x_y_h[i][2] != abs(C_X - x_y_h[i][0]) + abs(C_Y - x_y_h[i][1]) + H:
                        break
            else:
                print(C_X, C_Y, H)
                exit()

print("No")
