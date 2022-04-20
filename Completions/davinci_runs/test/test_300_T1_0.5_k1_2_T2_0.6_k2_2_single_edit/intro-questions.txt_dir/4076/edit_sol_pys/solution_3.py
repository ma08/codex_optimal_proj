#!/usr/bin/env python3

import sys
import re
import math

inp = sys.stdin.read()
inp = re.split("\n", inp)

a, b, h, m = [int(i) for i in inp[0].split()]

h_angle = h * 30 + m * 0.5
m_angle = m * 6

angle = math.fabs(h_angle - m_angle)

if angle > 180:
    angle = 360 - angle

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle * math.pi / 180)))
