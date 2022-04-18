

import math

a, b, c = list(map(int, input().split()))

p = (a + b + c) / 2

print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
