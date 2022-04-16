import sys

import math

h, v = [int(i) for i in sys.stdin.readline().split()]

v = v*math.pi/180

print(math.ceil(h/math.sin(v)))
