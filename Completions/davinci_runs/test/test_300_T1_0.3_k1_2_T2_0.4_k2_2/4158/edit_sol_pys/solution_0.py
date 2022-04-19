#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import os
import re

def main():
    n = int(input())
    x = list(map(int, input().split()))

    x.sort()

ans = []
for i in range(n):
    for j in range(i+1, n):
        if d.get(x[j] - x[i], 0) > 1:
            ans.append(x[i])
            ans.append(x[j])
            d[x[j] - x[i]] -= 2

print(len(ans))
print(*ans)
