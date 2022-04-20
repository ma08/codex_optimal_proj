
import math

abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

if a >= b and a >= c:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
elif b >= a and b >= c:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
else:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
