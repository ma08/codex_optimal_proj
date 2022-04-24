

import sys

N = int(input())

break_flag = False
break_flag2 = False
break_flag3 = False
break_flag4 = False
break_flag5 = False
break_flag6 = False
break_flag7 = False
break_flag8 = False
break_flag9 = False
break_flag10 = False
x_y_h = []
for i in range(N):
    x_y_h.append(list(map(int, sys.stdin.readline().split())))

    for j in range(N):
        for k in range(N):
            if x_y_h[i][0] == x_y_h[j][0] and x_y_h[i][1] != x_y_h[j][1] and x_y_h[i][2] == x_y_h[j][2]:
                C_X = x_y_h[i][0]
                C_Y = (x_y_h[i][1] + x_y_h[j][1]) / 2
                H = abs(x_y_h[i][1] - x_y_h[j][1]) + x_y_h[i][2]
            elif x_y_h[i][0] != x_y_h[j][0] and x_y_h[i][1] == x_y_h[j][1] and x_y_h[i][2] == x_y_h[j][2]:
                C_X = (x_y_h[i][0] + x_y_h[j][0]) / 2
                C_Y = x_y_h[i][1]
                H = abs(x_y_h[i][0] - x_y_h[j][0]) + x_y_h[i][2]
            elif x_y_h[i][0] == x_y_h[j][0] and x_y_h[i][1] == x_y_h[j][1] and x_y_h[i][2] != x_y_h[j][2]:
                print("No")
                exit()
            elif x_y_h[i][0] == x_y_h[k][0] and x_y_h[i][1] != x_y_h[k][1] and x_y_h[i][2] == x_y_h[k][2]:
                C_X = x_y_h[i][0]
                C_Y = (x_y_h[i][1] + x_y_h[k][1]) / 2
                H = abs(x_y_h[i][1] - x_y_h[k][1]) + x_y_h[i][2]
            elif x_y_h[i][0] != x_y_h[k][0] and x_y_h[i][1] == x_y_h[k][1] and x_y_h[i][2] == x_y_h[k][2]:
                C_X = (x_y_h[i][0] + x_y_h[k][0]) / 2
                C_Y = x_y_h[i][1]
                H = abs(x_y_h[i][0] - x_y_h[k][0]) + x_y_h[i][2]
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
