

import sys
import math

a, b, h, m = [int(i) for i in sys.stdin.readline().split()]

h_angle = h * 30 + m * 0.5  # 時針の角度
m_angle = m * 6  # 分針の角度
angle = math.fabs(h_angle - m_angle)  # 時針と分針の角度の差

if angle > 180:
    angle = 360 - angle  # 差が180度を超える場合、360度から差を引く

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle * math.pi / 180)))
