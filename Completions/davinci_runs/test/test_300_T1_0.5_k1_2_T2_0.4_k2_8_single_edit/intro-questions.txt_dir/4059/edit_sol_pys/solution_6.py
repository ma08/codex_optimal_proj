#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://atcoder.jp/contests/abc093/tasks/arc094_a

n = int(input())

ans = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        c = n - a * b
        if c > 0:
            ans += 1

print(ans)
