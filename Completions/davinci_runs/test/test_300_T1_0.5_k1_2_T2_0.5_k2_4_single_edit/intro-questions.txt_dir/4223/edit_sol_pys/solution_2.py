
# coding: utf-8

from collections import Counter

n = int(input())
s = input().split()

a = Counter(s)

ans = n - sum(a.values())

print(ans)
