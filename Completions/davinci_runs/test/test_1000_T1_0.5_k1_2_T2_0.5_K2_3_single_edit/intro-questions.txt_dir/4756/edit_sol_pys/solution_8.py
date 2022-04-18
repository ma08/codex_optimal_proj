
import sys

N = int(sys.stdin.readline())

points = []

for i in range(N):
    points.append(list(map(int, sys.stdin.readline().split())))

points = sorted(points, key=lambda p: p[1])

min_a = float("inf")

for i in range(N):
    if i == N - 1:
        break

    a = (points[i][0] + points[i][1] - points[i + 1][0] - points[i + 1][1]) / 2.0
    min_a = min(min_a, a)

print(min_a)
