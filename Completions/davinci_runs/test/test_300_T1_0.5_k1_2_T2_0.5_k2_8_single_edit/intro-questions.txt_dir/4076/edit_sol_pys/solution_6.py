#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import math
import numpy as np
a, b, h, m = [int(i) for i in sys.stdin.readline().split()]

h_angle = h * 30 + m * 0.5
m_angle = m * 6

angle = math.fabs(h_angle - m_angle)

if angle > 180:
    angle = 360 - angle

print(np.sqrt(a ** 2 + b ** 2 - 2 * a * b * np.cos(angle * np.pi / 180)))
