#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = input()
t = input()

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)
