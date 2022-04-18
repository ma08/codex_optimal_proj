

import math
import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split())

a = []
b = []

for i in range(n):    
    a.append(int(sys.stdin.readline()))
    b.append(int(sys.stdin.readline()))

c = []
for i in range(n):
    c.append(b[i] / a[i])


print(math.floor(sum(a) * max(c)))
