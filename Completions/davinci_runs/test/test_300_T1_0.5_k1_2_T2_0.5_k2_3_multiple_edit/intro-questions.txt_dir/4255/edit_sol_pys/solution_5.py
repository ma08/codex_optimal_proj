import math

a, b, c = int(input()), int(input()), int(input())

p = (a + b + c) / 2
print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
