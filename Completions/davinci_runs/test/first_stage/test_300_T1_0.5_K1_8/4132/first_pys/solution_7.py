

import numpy as np

n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

for i in range(n-1):
    a[i+1] = min(a[i+1], a[i])

print(a[-1])