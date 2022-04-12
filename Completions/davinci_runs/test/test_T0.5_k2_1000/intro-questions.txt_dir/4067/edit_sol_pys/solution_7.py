#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:35:33 2020

@author: hihyun
"""


n = int(input())
s = input()

#s = '120110'
#n = len(s)

a = [0, 0, 0]
for i in range(n):
    a[int(s[i])] += 1

#print(a)

if a[1] == a[2]:
    print(s)
else:
    r = abs(a[1] - a[2]) // 3
    #print(r)
    a[1] -= r
    a[2] += r
    #print(a)
    ans = ''
    for i in range(n):
        if a[0] > 0:
            ans += '0'
            a[0] -= 1
        elif a[1] > 0:
            ans += '1'
            a[1] -= 1
        elif a[2] > 0:
            ans += '2'
            a[2] -= 1
    print(ans)
