
import math

n = float(input())

def f(x):
    return math.pow(x, x) - n

a = 0.5
b = 2

while abs(b - a) > 1e-5:
    c = (a + b) / 2
    if f(c) > 0:
        b = c
    else:
        a = c

print(a)
