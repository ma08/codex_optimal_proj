
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
                CX = x_y_h[i][0]
                CY = (x_y_h[i][1] + x_y_h[j][1]) / 2
                if x_y_h[i][2] == x_y_h[j][2]:
                    H = abs(x_y_h[i][1] - x_y_h[j][1]) + x_y_h[i][2]
                else:
                    H = abs(x_y_h[i][1] - x_y_h[j][1]) + max(x_y_h[i][2], x_y_h[j][2])
                break
for i in range(N):
    if x_y_h[i][0] == CX and x_y_h[i][1] == CY:
        if x_y_h[i][2] != H:
            print("No")
            exit()
    else:
        if x_y_h[i][2] != abs(CX - x_y_h[i][0]) + abs(CY - x_y_h[i][1]) + H:
            print("No")
            exit()
print(CX, CY, H)
