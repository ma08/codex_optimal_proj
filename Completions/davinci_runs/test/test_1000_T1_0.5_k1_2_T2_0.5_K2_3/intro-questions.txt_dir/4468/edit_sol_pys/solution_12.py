
import sys

N, T = map(int, sys.stdin.readline().split())

# 1
# x = 0   # python 2.x
# for i in range(N):
#     t = int(sys.stdin.readline())
#     x = max(x, t)
# print(x + T)  # python 2.x

# 2
t = [0] * N  # python 2.x
for i in range(N):
    t[i] = int(sys.stdin.readline())
print(max(t) + T)  # python 2.x
