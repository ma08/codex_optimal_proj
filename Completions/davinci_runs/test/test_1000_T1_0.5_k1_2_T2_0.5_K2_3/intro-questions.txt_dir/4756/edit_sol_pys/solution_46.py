

import sys

N = int(sys.stdin.readline())

points = []

for i in range(N):
    points.append(map(int, sys.stdin.readline().split()))

points = sorted(points, key = lambda p: p[1])

min_x = float("inf")

for i in range(N):
    if i == N - 1:
        break
    
    x = (points[i][0] + points[i][1] - points[i + 1][0] - points[i + 1][1]) / 2.0
    min_x = min(min_x, x)

print min_x
