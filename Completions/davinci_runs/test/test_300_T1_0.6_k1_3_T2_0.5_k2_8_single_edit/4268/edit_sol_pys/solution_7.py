

import math # for sqrt

N, D = list(map(int, input().split()))
points = list() # list of points

for i in range(N): # add all points to list
    points.append(list(map(int, input().split())))

num_pairs = 0 # number of pairs of points

for i in range(N): # loop through points
    for j in range(i + 1, N): # loop through points after i
        distance = 0
        for k in range(D):
            distance += (points[i][k] - points[j][k]) ** 2
        distance = math.sqrt(distance)

        if distance % 1 == 0:
            num_pairs += 1

print(num_pairs)
