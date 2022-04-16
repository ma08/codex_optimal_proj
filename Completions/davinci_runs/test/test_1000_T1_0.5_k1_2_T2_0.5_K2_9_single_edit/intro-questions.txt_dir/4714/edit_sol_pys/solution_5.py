import math
N, D = map(int, input().split())


x = [list(map(int, input().split())) for i in range(N)]

count = 0

for i in range(N):
    for j in range(i + 1, N):
        distance = 0
        for k in range(D):
            distance += (x[i][k] - x[j][k]) ** 2
        if math.sqrt(distance).is_integer():
        count += 1

print(count)
