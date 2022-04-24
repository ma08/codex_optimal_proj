# -*- coding: utf-8 -*-
import sys

s = input()
t = input()

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1
sys.stdin.close()
print(ans)
