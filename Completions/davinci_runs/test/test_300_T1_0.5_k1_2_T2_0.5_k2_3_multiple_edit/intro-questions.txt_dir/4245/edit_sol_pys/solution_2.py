import math
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

if K == 0:
    print(N * N)
    exit()

count = 0
for b in range(1, N + 1):
    p = math.floor(N / b)
    count += p * max(0, b - K)
    count += max(0, N - p * b - K + 1)
print(count)
