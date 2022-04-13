import math

l = int(input())

if l % 2 == 0:
    a = l / 2
    b = l / 2
    c = l / 2
else:
    a = (l - math.sqrt(l)) / 3
    b = (l + math.sqrt(l)) / 3
    c = l / 2

print(a * b * c)
