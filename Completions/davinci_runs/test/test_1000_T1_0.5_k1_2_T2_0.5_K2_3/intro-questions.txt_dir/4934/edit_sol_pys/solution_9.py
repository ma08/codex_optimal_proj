# this is a comment

import sys
import math

h, v = [float(i) for i in sys.stdin.readline().split()]

print(math.ceil(h/math.sin(math.radians(v))))
