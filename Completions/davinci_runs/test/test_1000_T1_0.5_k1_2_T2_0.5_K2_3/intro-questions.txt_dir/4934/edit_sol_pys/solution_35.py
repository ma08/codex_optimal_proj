# this is a comment and a syntax error

import sys
import math

h, v = [int(i) for i in sys.stdin.readline().split()]

print(math.ceil(h/math.sin(math.radians(v))))
