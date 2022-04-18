# coding: utf-8
n, t = map(int, input().split())
ans = 10**9
for i in range(n):
    c, tt = map(int, input().split())
    if tt <= t:
        ans = min(ans, c)
print(ans if ans < 10**9 else 'TLE')
