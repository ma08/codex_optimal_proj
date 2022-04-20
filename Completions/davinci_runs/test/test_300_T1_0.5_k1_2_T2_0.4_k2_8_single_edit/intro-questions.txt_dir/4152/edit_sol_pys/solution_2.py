
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/05/19
# Feature:  # Enter feature name here
# Proble:
# Solution

n = int(input())
a = list(map(int, input().split()))

s = set()
for i in range(n):
    if a[i] not in s:
        s.add(a[i])
    else:
        s.remove(a[i])

print(n - len(s))
