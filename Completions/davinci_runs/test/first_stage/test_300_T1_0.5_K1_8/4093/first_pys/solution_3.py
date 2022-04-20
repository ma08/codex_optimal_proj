

import math

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print((n-1)*min(m, n-m))