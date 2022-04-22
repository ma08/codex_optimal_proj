#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

ans = 0
for i in d:
    ans += d[i] - 2

print(ans)
