#input
import math

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
else:
    print('Not a triangle')
