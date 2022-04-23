# -*- coding: utf-8 -*-

import sys
import math

# 入力
a, b, h, m = [int(i) for i in sys.stdin.readline().split()]

# 角度を計算
h_angle = h * 30 + m * 0.5
m_angle = m * 6

# 2つの時計の針の角度の差を計算
angle = math.fabs(h_angle - m_angle)

# 角度が180度より大きい場合
if angle > 180:
    angle = 360 - angle
# 出力

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle * math.pi / 180)))
