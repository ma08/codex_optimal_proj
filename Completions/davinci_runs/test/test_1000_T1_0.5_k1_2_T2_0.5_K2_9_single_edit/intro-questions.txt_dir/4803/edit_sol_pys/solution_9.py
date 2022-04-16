

import math

N = int(input())

def f(x):
    return math.pow(x, x) - N 

a = 1
b = N

while b - a > 0.0000001:
    c = (a + b) / 2
    if f(c) > 0:
        b = c
    else:
        a = c

print(a)
