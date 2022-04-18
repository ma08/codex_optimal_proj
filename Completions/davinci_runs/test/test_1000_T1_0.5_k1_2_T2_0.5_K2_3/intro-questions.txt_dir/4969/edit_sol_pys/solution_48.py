
from math import pi, acos, sin

R, C = map(int, input().split())  # R is the outer radius of the ring and C is the radius of the hole

r = R - C  # r is the inner radius

A = pi * r * r  # A is the area of the ring
B = pi * R * R  # B is the area of the circle

print(A/B * 100)  # print the percentage of the ring
