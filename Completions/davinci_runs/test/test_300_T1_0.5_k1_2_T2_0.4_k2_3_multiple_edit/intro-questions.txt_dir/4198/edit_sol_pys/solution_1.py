# coding: utf-8
import math
a, b, h, m = map(int, input().split())
h = math.radians(h * 30 + m * 0.5)
m = math.radians(m * 6)
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(h - m)))
