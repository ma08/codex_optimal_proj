import math

R, C = map(int, input().split())

r = R - C

A = math.pi * r * r
B = math.pi * R * R

print(A/B * 100)
