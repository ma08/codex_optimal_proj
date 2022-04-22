

import sys

N = int(input())

x_y_h = []
for i in range(N):
    x_y_h.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(i+1, N):
        if x_y_h[i][0] == x_y_h[j][0]:
            if x_y_h[i][1] == x_y_h[j][1]:
                if x_y_h[i][2] != x_y_h[j][2]:
                    print("No")
                    exit()
            else:
                C_X = x_y_h[i][0]
                C_Y = (x_y_h[i][1] + x_y_h[j][1]) / 2
                if x_y_h[i][2] == x_y_h[j][2]:
                    H = abs(x_y_h[i][1] - x_y_h[j][1]) + x_y_h[i][2]
                else:
                    H = abs(x_y_h[i][1] - x_y_h[j][1]) + max(x_y_h[i][2], x_y_h[j][2])
                break
        elif x_y_h[i][1] == x_y_h[j][1]:
            if x_y_h[i][2] == x_y_h[j][2]:
                C_X = (x_y_h[i][0] + x_y_h[j][0]) / 2
                C_Y = x_y_h[i][1]
                H = abs(x_y_h[i][0] - x_y_h[j][0]) + x_y_h[i][2]
                break
            else:
                C_X = (x_y_h[i][0] + x_y_h[j][0]) / 2
                C_Y = x_y_h[i][1]
                H = abs(x_y_h[i][0] - x_y_h[j][0]) + max(x_y_h[i][2], x_y_h[j][2])
                break
        else:
            if x_y_h[i][2] != x_y_h[j][2]:
                print("No")
                exit()
            else:
                C_X = (x_y_h[i][0] + x_y_h[j][0]) / 2
                C_Y = (x_y_h[i][1] + x_y_h[j][1]) / 2
                H = abs(x_y_h[i][0] - x_y_h[j][0]) + abs(x_y_h[i][1] - x_y_h[j][1]) + x_y_h[i][2]
                break
            
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
