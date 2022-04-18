#!/usr/bin/env python3

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = -1
    if n == 1:
        ans = a[0]
    else:
        for i in range(n-1):
            if a[i] > a[i+1] - k:
                ans = a[i+1] - k
                break
    print(ans)
