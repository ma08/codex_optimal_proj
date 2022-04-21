

import math

N, D = map(int, input().split())

X = [list(map(int, input().split())) for i in range(N)]

count = 0

for i in range(N):
    for j in range(i+1, N):
        dist = 0
        for k in range(D):
            dist += (X[i][k]-X[j][k])**2
        if math.sqrt(dist) % 1 == 0:
            count += 1

print(count)
