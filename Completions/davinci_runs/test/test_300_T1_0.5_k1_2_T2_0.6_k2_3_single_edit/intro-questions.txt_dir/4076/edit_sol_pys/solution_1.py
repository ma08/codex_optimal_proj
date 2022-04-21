import sys
import math
from decimal import *



a, b, h, m = [Decimal(i) for i in sys.stdin.readline().split()]

h_angle = h * 30 + m * 0.5
m_angle = m * 6

angle = math.fabs(h_angle - m_angle)

if angle > 180:
    angle = 360 - angle

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(Decimal(angle) * math.pi / 180)))
