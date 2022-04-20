

import sys

# define input
N, M = map(int, input().split())
L = [0] * M
R = [0] * M
for i in range(M):
    L[i], R[i] = map(int, input().split())

# calculate
pass_num = [0] * (N + 1)
for i in range(M):
    pass_num[L[i]] += 1
    pass_num[R[i] + 1] -= 1
for i in range(1, N + 1):
    pass_num[i] += pass_num[i - 1]

print(pass_num.count(M))