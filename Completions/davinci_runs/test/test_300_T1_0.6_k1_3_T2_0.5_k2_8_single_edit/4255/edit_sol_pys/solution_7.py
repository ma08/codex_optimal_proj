import math

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
s = (a + b + c) / 2
print(math.sqrt(s * (s - a) * (s - b) * (s - c)))
