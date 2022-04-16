from math import pi, acos, sin
R, C = map(int, input().split())
r = R - C
A = pi * r * r
B = pi * R * R
print(A/B * 100)
