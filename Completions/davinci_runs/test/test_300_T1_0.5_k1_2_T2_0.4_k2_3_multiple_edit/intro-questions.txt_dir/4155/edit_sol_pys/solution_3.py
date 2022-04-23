# -*- coding: utf-8 -*-

n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        h[i+1] = h[i]
    else:
        ans = i+1
        break

print(ans)
