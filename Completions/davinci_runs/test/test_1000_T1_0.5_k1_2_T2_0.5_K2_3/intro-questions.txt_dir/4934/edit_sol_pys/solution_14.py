import sys
import math
import numpy as np

# input
h, v = map(float, sys.stdin.readline().split())

# calculate
a = math.radians(v)
b = np.sin(a)
c = h / b
d = math.ceil(c)

# output
print(d)
