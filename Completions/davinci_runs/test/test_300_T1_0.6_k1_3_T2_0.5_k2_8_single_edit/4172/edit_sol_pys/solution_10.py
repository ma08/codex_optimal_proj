#!/usr/bin/env python3
n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(0)
else:
    mi = min(a)
    mx = max(a)
    if abs(mi - mx) == 0:
        print(0)
    else:
        ans = abs(mi - mx)
        while k < n:
            ans -= 1
            k += 1
        print(ans)
