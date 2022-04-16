import sys

N, T = map(int, sys.stdin.readline().rstrip().split())
t = list(map(int, sys.stdin.readline().rstrip().split()))

total = 0
start = 0

for i in range(N):
    if t[i] < start:
        total += T
    else:
        total += T + t[i] - start
        start = t[i]

print(total)
