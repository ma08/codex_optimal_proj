# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

cnt = 0
tmp = 0

for i in range(n):
    if i == 0:
        tmp = a[i]
    else:
        if tmp > a[i]:
            cnt += 1
        tmp = a[i]

print(cnt)
