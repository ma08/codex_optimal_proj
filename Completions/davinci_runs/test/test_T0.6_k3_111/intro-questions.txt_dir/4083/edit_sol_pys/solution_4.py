

import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

min_val = min(a)

count = 0
for i in range(n):
    a[i] -= min_val
    count += a[i] // 2

if count >= k - 1:
    print(math.ceil((count - k + 1) / (k-1)))
else:
    print(-1)
