
import sys

N, M = map(int, sys.stdin.readline().split())

t = [0] * N
for i in range(N):
    t[i] = int(sys.stdin.readline())
print(max(t) + M)
