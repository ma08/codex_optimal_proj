
import math

L = int(input())

if L % 2 == 0:
    a = L / 2
    b = L / 2
    c = L / 2
else:
    a = (L - math.sqrt(L)) / 2
    b = (L + math.sqrt(L)) / 2
    c = L / 2

print(a * b * c)
