
from math import pi

R, C = map(int, input().split())  # R is the outer radius of the ring and C is the radius of the hole

r = R - C  # r is the inner radius

A = pi * r * r  # A is the area of the ring
B = pi * R * R  # B is the area of the circle

print(A/B * 100)
