
import math

def f(x):
    return math.exp(x * math.log(2)) - 2.0

l, r = 0.0, 2.0

while r - l > 1e-9:  # 1e-9 = 1 * 10^(-9)
    m = (l + r) / 2.0
    if f(m) < 0:
        l = m
    else:
        r = m

print(l)
