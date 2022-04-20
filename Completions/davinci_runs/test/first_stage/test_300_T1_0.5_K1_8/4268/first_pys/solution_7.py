

import sys
from math import sqrt

# read input
N, D = map(int, sys.stdin.readline().split())

points = []
for _ in range(N):
    points.append(list(map(int, sys.stdin.readline().split())))

# brute force
count = 0
for i in range(N):
    for j in range(i):
        dist = 0
        for k in range(D):
            dist += (points[i][k] - points[j][k])**2
        dist = sqrt(dist)
        if dist == int(dist):
            count += 1

print(count)