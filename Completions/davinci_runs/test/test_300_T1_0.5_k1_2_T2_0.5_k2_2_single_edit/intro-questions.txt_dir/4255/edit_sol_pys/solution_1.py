



def get_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

import math

abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

if a >= b and a >= c:
    if b >= c:
        print(get_area(a, b, c))
    else:
        print(get_area(a, c, b))
elif b >= a and b >= c:
    if a >= c:
        print(get_area(b, a, c))
    else:
        print(get_area(b, c, a))
else:
    if a >= b:
        print(get_area(c, a, b))
    else:
        print(get_area(c, b, a))
