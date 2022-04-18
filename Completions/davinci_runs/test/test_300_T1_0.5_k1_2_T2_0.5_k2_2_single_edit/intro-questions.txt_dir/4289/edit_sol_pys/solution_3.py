# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline

n = int(input())
s = list(input())
ans = 0

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        ans += 1

print(diff.index(min(diff)) + 1)
