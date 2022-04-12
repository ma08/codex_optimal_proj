
import sys

N, T = map(int, sys.stdin.readline().rstrip().split())
t = list(map(int, sys.stdin.readline().split()))

total = 0
prev = 0

for i in range(N):
    if t[i] < prev:
        total += T
    else:
        total += T + t[i] - prev
        prev = t[i]

print(total)
