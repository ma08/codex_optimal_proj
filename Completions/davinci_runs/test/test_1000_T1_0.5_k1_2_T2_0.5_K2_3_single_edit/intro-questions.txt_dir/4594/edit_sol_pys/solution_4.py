import collections

import sys

N, M = map(int, sys.stdin.readline().split())

d_list = [0] * N
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    d_list[a-1] += 1
    d_list[b-1] += 1

for i in d_list:
    print(i)
