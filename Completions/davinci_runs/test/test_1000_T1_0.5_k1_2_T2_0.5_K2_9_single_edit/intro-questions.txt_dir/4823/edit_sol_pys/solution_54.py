
from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c
if d == 0:
    print(-b/(2*a))
elif d > 0:
    print((-b+sqrt(d))/(2*a))
    print((-b-sqrt(d))/(2*a))
