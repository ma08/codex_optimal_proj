

import math  # import math module
# read input

# separate input
abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])
# first if

if a >= b and a >= c:
    if b >= c:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    else:
        p = (a + b + c) / 2
# second if
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
elif b >= a and b >= c:
    if a >= c:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    else:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
else:
    if a >= b:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    else:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
