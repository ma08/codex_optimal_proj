

import math

n = int(input())
d = list(map(int, input().split()))

x = 1
y = 1
for i in range(n):
    if d[i] in d[i+1:]:
        x = x * d[i]
    else:
        y = y * d[i]

print(x,y)