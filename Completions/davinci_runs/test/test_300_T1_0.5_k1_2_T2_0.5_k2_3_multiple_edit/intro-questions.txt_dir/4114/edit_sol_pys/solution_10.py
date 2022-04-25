
import sys


def is_answer(x, y, h):
    for i in range(N):
        if x_y_h[i][0] == x and x_y_h[i][1] == y:
            if x_y_h[i][2] != h:
                return False
        else:
            if x_y_h[i][2] != abs(x - x_y_h[i][0]) + abs(y - x_y_h[i][1]) + h:
                return False
    return True


N = int(input())

x_y_h = []
for i in range(N):
    x_y_h.append(list(map(int, sys.stdin.readline().split())))

C_X = 0
C_Y = 0
H = 0

for i in range(N):
    for j in range(i+1, N):
        if x_y_h[i][0] == x_y_h[j][0] and x_y_h[i][1] == x_y_h[j][1]:
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

if is_answer(C_X, C_Y, H):
    print(C_X, C_Y, H)
elif is_answer(C_X + 1, C_Y, H - 1):
    print(C_X + 1, C_Y, H - 1)
elif is_answer(C_X - 1, C_Y, H - 1):
    print(C_X - 1, C_Y, H - 1)
else:
    print("No")
