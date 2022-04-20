

import math

N, D = list(map(int, input().split()))
points = list()

for i in range(N):
    points.append(list(map(int, input().split())))

num_pairs = 0

for i in range(N):
    for j in range(i + 1, N):
        distance = 0
        for k in range(D):
            distance += (points[i][k] - points[j][k]) ** 2
        distance = math.sqrt(distance)

        if distance % 1 == 0:
            num_pairs += 1

print(num_pairs)