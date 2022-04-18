
import sys

N, T = map(int, sys.stdin.readline().split())

# 1.
# x = 0
# for i in range(N):
#     t = int(sys.stdin.readline())
#     x = max(x, t)
# print(x + T)

# 2.
# t = [0] * N
# for i in range(N):
#     t[i] = int(sys.stdin.readline())
# print(max(t) + T)

# 3.
# t = []
# for i in range(N):
#     t.append(int(sys.stdin.readline()))
# print(max(t) + T)

# 4.
# t = []
# for i in range(N):
#     t.append(int(input()))
# print(max(t) + T)

# 5.
# t = [int(input()) for i in range(N)]
# print(max(t) + T)

# 6.
print(max([int(input()) for i in range(N)]) + T)
