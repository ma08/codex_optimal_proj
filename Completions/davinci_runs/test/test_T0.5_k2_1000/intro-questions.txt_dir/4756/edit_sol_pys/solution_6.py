
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

minimum = 10**6

for i in range(n):
    if fabs(x[i] - y[i]) < minimum:
        minimum = fabs(x[i] - y[i])

print(minimum)
