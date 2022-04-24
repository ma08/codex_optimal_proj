import math

N, X = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

x.sort()

dist = 0
for i in range(1, N):
    d = x[i] - x[i - 1]
    dist += d * (i * (N - i))

print(dist * 2 * math.pi * X)
