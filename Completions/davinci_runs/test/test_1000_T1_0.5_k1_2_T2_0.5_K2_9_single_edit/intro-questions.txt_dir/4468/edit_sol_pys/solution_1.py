
import sys

N, T = map(int, sys.stdin.readline().split())

# 1.
x = 0
for i in range(N):
    t = int(sys.stdin.readline())
    x = max(x, t)
print(x + T)

# 2.
t = [0] * N
for i in range(N):
    t[i] = int(sys.stdin.readline())
print(max(t) + T)
