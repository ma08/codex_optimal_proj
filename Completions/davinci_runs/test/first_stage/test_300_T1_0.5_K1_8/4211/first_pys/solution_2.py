

import sys

n = int(input())
b = list(map(int, input().split()))

a = [0] * n
a[0] = b[0]
a[-1] = b[-1]

for i in range(n-2, 0, -1):
    a[i] = b[i] - max(a[i], a[i+1])

print(sum(a))