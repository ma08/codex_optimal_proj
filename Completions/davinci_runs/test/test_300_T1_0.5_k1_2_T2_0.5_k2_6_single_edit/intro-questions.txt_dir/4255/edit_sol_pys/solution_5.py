

import math

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a >= b and a >= c:
    if b >= c:
        p = (a + b + c) / 2.0
        print('{:.1f}'.format(math.sqrt(p * (p - a) * (p - b) * (p - c))))
    else:
        p = (a + b + c) / 2.0
        print('{:.1f}'.format(math.sqrt(p * (p - a) * (p - b) * (p - c))))
elif b >= a and b >= c:
    if a >= c:
        print('{:.1f}'.format(math.sqrt(p * (p - a) * (p - b) * (p - c))))
    else:
        p = (a + b + c) / 2.0
        print('{:.1f}'.format(math.sqrt(p * (p - a) * (p - b) * (p - c))))
else:
    if a >= b:
        p = (a + b + c) / 2.0
        print('{:.1f}'.format(math.sqrt(p * (p - a) * (p - b) * (p - c))))
    else:
        p = (a + b + c) / 2.0
        print('{:.1f}'.format(math.sqrt(p * (p - a) * (p - b) * (p - c))))
