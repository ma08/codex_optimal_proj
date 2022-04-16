import sys
from math import sqrt

a, b, c = sys.stdin.read().split()

a = int(a)
b = int(b)
c = int(c)

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
