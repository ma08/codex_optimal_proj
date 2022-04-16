
#

import sys
from math import sqrt, fabs

n = int(sys.stdin.readline())

x = []
y = []

for i in range(n):
    data = sys.stdin.readline().split()
    x.append(int(data[0]))
    y.append(int(data[1]))

x.sort()
y.sort()

min = 10**6

for i in range(n):
    if fabs(x[i] - y[i]) < min:
        min = fabs(x[i] - y[i])

print(min)
