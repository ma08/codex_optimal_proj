



def area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

import math

abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

if a >= b and a >= c:
    if b >= c:
        print(area(a, b, c))
    else:
        print(area(a, b, c))
elif b >= a and b >= c:
    if a >= c:
        print(area(a, b, c))
    else:
        print(area(a, b, c))
else:
    if a >= b:
        print(area(a, b, c))
    else:
        print(area(a, b, c))
