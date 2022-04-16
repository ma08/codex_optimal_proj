

import math

abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

if a >= b + c or b >= a + c or c >= a + b:
    print("impossible")
else:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
