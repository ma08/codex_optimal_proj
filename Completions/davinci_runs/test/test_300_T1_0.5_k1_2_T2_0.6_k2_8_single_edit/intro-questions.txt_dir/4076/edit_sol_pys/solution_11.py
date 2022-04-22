
import sys
import math

a, b, h, m = [int(i) for i in sys.stdin.readline().split()]

h_angle = h * 30 + m * 0.5
m_angle = m * 6
angle = math.fabs(h_angle - m_angle)

if angle > 180:
    angle = 360 - angle
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle * math.pi / 180)))
