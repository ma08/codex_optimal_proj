
from sys import stdin

N, M = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

A.sort()

count = 0

for i in range(0, N, M):
    count += 1

    for j in range(i, i + M - 1):
        if abs(A[j] - A[j + 1]) > 0:
            count += 1
            break

print(count)
