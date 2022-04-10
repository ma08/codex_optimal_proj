# coding: utf-8

n,k,m = map(int,input().split())
a = list(map(int,input().split()))

s = sum(a)

if m*n - s > k: # m*n - s の最大値はk
    print(-1)
else:
    print(m*n - s)
