# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 19:56:24 2018
@author: 李弘一萌
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
s = 0
for i in range(n):
    for j in range(n):
        if b[i] > c[j]:
            s += 1
print(s)
