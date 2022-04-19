
import sys

N = int(input())

x_y_h = []
for i in range(N):
    x_y_h.append(list(map(int, sys.stdin.readline().split())))

for i in range(100):
    for j in range(100):
        for h in range(101):
            flag = True
            for k in range(N):
                if x_y_h[k][2] == 0:
                    if h > abs(x_y_h[k][0] - i) + abs(x_y_h[k][1] - j):
                        flag = False
                else:
                    if h != abs(x_y_h[k][0] - i) + abs(x_y_h[k][1] - j) + x_y_h[k][2]:
                        flag = False
            if flag:
                print(i, j, h)
                exit()

print("-1")
