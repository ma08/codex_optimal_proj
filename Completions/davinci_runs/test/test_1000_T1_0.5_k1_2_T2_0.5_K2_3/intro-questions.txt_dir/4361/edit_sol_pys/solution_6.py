# coding: utf-8

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

a = sorted(a)

ans = a[m-1] - a[0]

for i in range(n-m+1):
    if ans > a[i+m-1] - a[i]:
        ans = a[i+m-1] - a[i]

print(ans)
