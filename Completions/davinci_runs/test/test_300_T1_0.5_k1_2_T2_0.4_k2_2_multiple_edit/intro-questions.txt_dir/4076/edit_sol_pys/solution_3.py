
import sys
import math

a, b, h, m = map(int, sys.stdin.readline().split())

h_angle = (h * 30 + m * 0.5) * math.pi / 180
m_angle = (m * 6) * math.pi / 180

angle = abs(h_angle - m_angle)

if angle > 180:
    angle = 360 - angle

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle)))
