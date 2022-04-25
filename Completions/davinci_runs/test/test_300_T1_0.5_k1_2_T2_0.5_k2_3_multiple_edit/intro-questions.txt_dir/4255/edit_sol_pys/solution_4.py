import math

a, b, c = int(input()), int(input()), int(input())

if a >= b and a >= c:
    p = (a + b + c) / 2
    print(p * (p - a) * (p - b) * (p - c))
elif b >= a and b >= c:
    p = (a + b + c) / 2
    print(p * (p - a) * (p - b) * (p - c))
else:
    p = (a + b + c) / 2
    print(p * (p - a) * (p - b) * (p - c))
