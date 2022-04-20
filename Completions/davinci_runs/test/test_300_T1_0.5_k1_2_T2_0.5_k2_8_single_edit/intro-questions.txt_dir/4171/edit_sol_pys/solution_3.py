# -*- coding: utf-8 -*-

# Solution

n, k = map(int, input().split()) # n = 2, k = 2
a = list(map(int, input().split())) # a = [1, 2]

if k == 1:
    print(max(a))
else:
    print(max(a) - min(a) + 1)
