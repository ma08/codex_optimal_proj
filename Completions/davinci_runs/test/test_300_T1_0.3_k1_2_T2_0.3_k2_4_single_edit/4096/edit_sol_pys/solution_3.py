#!/usr/bin/python

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

if a[0] > m:
    print(-1)
else:
    days = 1
    curr = a[0]
    for i in range(1, n):
        if curr + a[i] > m:
            days += 1
            curr = a[i]
        else:
            curr += a[i]
    print(days)
