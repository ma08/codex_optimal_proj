
# -*- coding: utf-8 -*-

N = int(input())
h = [int(input()) for i in range(N)]

h.sort()
h.reverse()

max_h = h[0]
ans = 0
for i in range(1,N):
    if h[i] < max_h:
        ans += 1
        max_h = h[i]
print(ans)
