import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

min_time = A[0]
max_time = A[-1]

while min_time <= max_time:
    mid = (min_time + max_time) // 2
    cnt = 0

    for a in A:
        cnt += a // mid

    if cnt >= M:
        min_time = mid + 1
    else:
        max_time = mid - 1

print(max_time)
