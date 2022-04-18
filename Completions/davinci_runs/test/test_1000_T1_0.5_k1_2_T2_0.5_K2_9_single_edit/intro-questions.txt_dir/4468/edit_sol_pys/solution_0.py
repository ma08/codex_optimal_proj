
import sys

N, T = map(int, input().rstrip().split())
t = list(map(int, input().rstrip().split()))

total = T
start_time = 0

for i in range(N):
    if t[i] < start_time:
        total += T - start_time + t[i]
    else:
        total += T
    start_time = t[i]

print(total)
