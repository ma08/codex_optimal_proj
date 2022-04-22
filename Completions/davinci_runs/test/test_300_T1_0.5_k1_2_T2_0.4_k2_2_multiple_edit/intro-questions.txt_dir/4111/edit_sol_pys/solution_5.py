#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a,b,c = map(int,input().split())
#s = input()
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(N)]

n = int(input())
a = list(map(int,input().split()))

odd, even = 0, 0
for i in range(n):
    if i%2 == 0:
        odd += a[i]
    else:
        even += a[i]

ans = 0
for i in range(n):
    if i%2 == 0:
        if odd - a[i] == even:
            ans += 1
    else:
        if odd == even - a[i]:
            ans += 1

print(ans)
