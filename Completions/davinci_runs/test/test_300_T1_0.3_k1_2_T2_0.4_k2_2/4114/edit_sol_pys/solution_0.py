import sys

N = int(input())

# 入力を受け取る
points = []
for i in range(N):
    x, y, h = map(int, input().split())
    points.append([x, y, h])

# 入力を元に高さを求める
for cx in range(101):
    for cy in range(101):
        H = 0
        for i in range(N):
            H = max(H, points[i][2] + abs(points[i][0] - cx) + abs(points[i][1] - cy))
        if H > 0:
            print(cx, cy, H)
            sys.exit()
