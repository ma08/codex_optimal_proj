

import sys
import math

a, b, c = map(int, sys.stdin.readline().split())

if a >= b and a >= c:
    if b >= c:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{0:.2f}".format(S))
    else:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{0:.2f}".format(S))
elif b >= a and b >= c:
    if a >= c:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{0:.2f}".format(S))
    else:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{0:.2f}".format(S))
else:
    if a >= b:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{0:.2f}".format(S))
    else:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{0:.2f}".format(S))
