#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: alison

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = list(map(int, input().split()))

ans = 'Yes'

for i in range(m):
    sum = 0
    for j in range(n):
        sum += a[j][i]
    if sum < b[i]:
        ans = 'No'

if ans == 'No':
    print(ans)
else:
    print(ans)
    x = [0] * n
    for i in range(m):
        for j in range(n):
            if a[j][i] > 0:
                x[j] += b[i]
                break
    print(*x)
