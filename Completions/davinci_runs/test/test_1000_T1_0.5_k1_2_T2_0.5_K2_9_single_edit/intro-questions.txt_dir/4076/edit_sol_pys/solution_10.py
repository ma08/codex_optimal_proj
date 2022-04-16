

import sys
from math import sin, cos, pi

a, b, h, m = [int(i) for i in sys.stdin.readline().split()]

h_angle = h * 30 + m * 0.5
m_angle = m * 6

angle = abs(h_angle - m_angle)

if angle > 180:
    angle = 360 - angle

print(sin(angle * pi / 180) * a / cos(angle * pi / 180))
