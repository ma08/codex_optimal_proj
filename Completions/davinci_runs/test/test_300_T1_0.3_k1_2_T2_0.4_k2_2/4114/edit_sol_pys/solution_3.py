

import sys

N = int(input())
points = []
for i in range(N):
    x, y, h = map(int, input().split())
    points.append([x, y, h])
for cx in range(101):
    for cy in range(101):
        H = 0
        for i in range(N):
            H = max(H, points[i][2] + abs(points[i][0] - cx) + abs(points[i][1] - cy))
        if H > 0:
            print(cx, cy, H)
            sys.exit()
