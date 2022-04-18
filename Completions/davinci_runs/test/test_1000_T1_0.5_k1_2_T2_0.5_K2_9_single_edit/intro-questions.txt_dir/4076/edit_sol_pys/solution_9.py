

import sys
import numpy as np
import math

a, b, h, m = [int(i) for i in sys.stdin.readline().split()]

h_angle = np.deg2rad(h * 30 + m * 0.5)
m_angle = np.deg2rad(m * 6)

angle = abs(h_angle - m_angle)

if angle > np.pi:
    angle = 2 * np.pi - angle

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle)))
