#!/usr/bin/env python3

import math

h, v = [int(i) for i in input().split()]

v = v*math.pi/180

print(math.ceil(h/math.sin(v)))
