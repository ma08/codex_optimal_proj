
import sys
import math

h, v = [int(i) for i in input().split()]

print(math.ceil(h/math.sin(math.radians(v))))
