#!/usr/bin/env python
# coding: utf-8
N = int(input())

ans = 0
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        ans += 1
        if i != N // i:
            ans += 1

print(ans)
