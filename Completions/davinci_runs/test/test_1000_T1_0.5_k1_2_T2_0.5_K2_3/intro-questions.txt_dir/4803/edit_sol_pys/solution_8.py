
import math

N = float(input())
if N == 0:
    print(0)
else:
    def f(x):
        return math.pow(x, x) - N
    a = 0.5 # left border
    b = 2 # right border
    while b - a > 1e-5:
        c = (a + b) / 2
        if f(c) > 0:
            b = c
        else:
            a = c
    print(a)
