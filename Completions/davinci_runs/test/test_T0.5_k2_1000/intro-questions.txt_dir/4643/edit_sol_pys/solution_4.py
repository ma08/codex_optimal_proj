#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in a:
    print(i, end=' ')
