

import sys

N = int(input())

x_y_h = []
for i in range(N):
    x_y_h.append(list(map(int, sys.stdin.readline().split())))
                C_X = x_y_h[i][0]
                C_Y = (x_y_h[i][1] + x_y_h[k][1]) / 2
                H = abs(x_y_h[i][1] - x_y_h[k][1]) + x_y_h[i][2]
                break_flag = True
                break_flag2 = True
                break_flag3 = True
                break_flag4 = True
                break_flag5 = True
                break_flag6 = True
                break_flag7 = True
                break_flag8 = True
                break_flag9 = True
                break_flag10 = True
            elif x_y_h[i][0] != x_y_h[k][0] and x_y_h[i][1] == x_y_h[k][1] and x_y_h[i][2] == x_y_h[k][2]:
                C_X = (x_y_h[i][0] + x_y_h[k][0]) / 2
                C_Y = x_y_h[i][1]
                H = abs(x_y_h[i][0] - x_y_h[k][0]) + x_y_h[i][2]
                break_flag = True
                break_flag2 = True
                break_flag3 = True
                break_flag4 = True
                break_flag5 = True
                break_flag6 = True
                break_flag7 = True
                break_flag8 = True
                break_flag9 = True
                break_flag10 = True
            elif x_y_h[i][0] == x_y_h[k][0] and x_y_h[i][1] == x_y_h[k][1] and x_y_h[i][2] != x_y_h[k][2]:
                print("No")
                exit()
        if break_flag:
            break
    if break_flag2:
        break
    if break_flag3:
        break
    if break_flag4:
        break
    if break_flag5:
        break
    if break_flag6:
        break
    if break_flag7:
        break
    if break_flag8:
        break
    if break_flag9:
        break
    if break_flag10:
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
