#!/usr/bin/env python3
n, k = map(int, input().split())
a = list(map(int, input().split()))

if len(set(a)) < k:
    print('NO')
else:
    print('YES')
    for i in range(n):
        if k > 0 and a[i] not in a[:i]:
            print(i+1, end=' ')
            k -= 1
