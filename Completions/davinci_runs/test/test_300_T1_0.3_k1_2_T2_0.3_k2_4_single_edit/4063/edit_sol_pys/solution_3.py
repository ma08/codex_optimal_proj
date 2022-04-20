

import math

n, k = map(int, input().split())

ans = 0
for b in range(k + 1, n + 1):
    p = n // b
    r = n % b
    ans += (p * (p - 1) // 2) * (b - k)
    ans += p * (r - k + 1)
    if k == 0:
        ans -= p

print(ans)
