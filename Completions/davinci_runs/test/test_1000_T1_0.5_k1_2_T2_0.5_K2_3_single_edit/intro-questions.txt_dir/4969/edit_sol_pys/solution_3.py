
from math import pi, acos, sin, sqrt

R, C = map(int, input().split())

r = sqrt(R**2 - C**2)

A = pi * r * r
B = pi * R * R

print(A/B * 100)
