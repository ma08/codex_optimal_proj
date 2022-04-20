

from math import floor, ceil

x = float(input())

f = floor(x)
c = ceil(x)

if c - x < x - f:
    print(c, f)
else:
    print(f, c)