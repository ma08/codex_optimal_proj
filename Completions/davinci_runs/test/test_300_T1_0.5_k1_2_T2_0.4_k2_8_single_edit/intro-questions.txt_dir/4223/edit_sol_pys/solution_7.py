#!/usr/bin/env python3

from collections import Counter

n = int(input())
s = input()

c = Counter(s)

ans = n - sum(c.values())

print(ans)
