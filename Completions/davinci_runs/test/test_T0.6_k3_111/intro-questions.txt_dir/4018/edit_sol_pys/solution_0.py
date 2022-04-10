#!/usr/bin/env python3

n, k = map(int, input().split())
s = input()

if k > n*(n+1)//2:
    print(-1)
else:
    sm = 0
    p = 0
    for i in range(1, n+1):
        sm += i
        if sm >= k:
            p = i
            break
    print(n*(n+1)//2 - (p*(p+1)//2)) 
