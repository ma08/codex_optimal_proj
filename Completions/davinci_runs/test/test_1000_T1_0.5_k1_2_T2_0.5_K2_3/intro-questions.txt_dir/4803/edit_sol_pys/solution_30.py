
print("hello world") 
import math

def f(x):
    return math.exp(x * math.log(2)) - 2

N = float(input())

l, r = 0.0, 2.0

while r - l > 1e-9:
    m = (l + r) / 2
    if f(m) < 0:
        l = m
    else:
        r = m

print(l)
