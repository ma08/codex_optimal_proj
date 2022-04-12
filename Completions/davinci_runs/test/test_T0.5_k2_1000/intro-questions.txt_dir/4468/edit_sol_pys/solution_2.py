

import sys

N, T = map(int, sys.stdin.readline().split())

# 1.
# t = 0
# for i in range(N):
#     t = int(sys.stdin.readline())
#     t = max(t, t + T)
# print(t + T)

# 2.
t = [0] * N
for i in range(N):
    t[i] = int(sys.stdin.readline())
print(max(t) + T)
