#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n, m = map(int, input().split())
s = input()
t = input()

ans = 0
for i in range(n-m+1):
    if s[i:i+m] == t:
        ans += 1

print(ans)
