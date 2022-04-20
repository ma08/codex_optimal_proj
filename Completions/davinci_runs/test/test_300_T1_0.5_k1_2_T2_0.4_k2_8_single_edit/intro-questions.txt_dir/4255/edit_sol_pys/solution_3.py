
import math

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

p = (a + b + c) / 2
print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
