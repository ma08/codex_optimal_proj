import math

a, b, c = float(input()), float(input()), float(input())

if a >= b and a >= c:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c))
elif b >= a and b >= c:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c))
else:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c))
