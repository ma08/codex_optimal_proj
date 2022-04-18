


# input
# 3
# 1 1 5
# 3 3 5
# 3 1 5
# output
# 3 2 5
import sys

N = int(input())

x_y_h = []
for i in range(N):
    x_y_h.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(i+1, N):
        if x_y_h[i][0] == x_y_h[j][0] and x_y_h[i][1] == x_y_h[j][1]:
            if x_y_h[i][2] != x_y_h[j][2]:
                print("No")
                exit()
            else:  # x_y_h[i][2] == x_y_h[j][2]
                C_X = x_y_h[i][0]  # C_X == x_y_h[j][0]
                C_Y = (x_y_h[i][1] + x_y_h[j][1]) / 2  # C_Y == (x_y_h[i][1] + x_y_h[j][1]) / 2
                H = x_y_h[i][2]  # H == x_y_h[i][2] == x_y_h[j][2]
                break  # break out of loop

for i in range(N):
    if x_y_h[i][0] == C_X and x_y_h[i][1] == C_Y and x_y_h[i][2] != H:
        print("No")
        exit()
    elif x_y_h[i][2] != abs(C_X - x_y_h[i][0]) + abs(C_Y - x_y_h[i][1]) + H:
        print("No")
        exit()

print(C_X, C_Y, H)
