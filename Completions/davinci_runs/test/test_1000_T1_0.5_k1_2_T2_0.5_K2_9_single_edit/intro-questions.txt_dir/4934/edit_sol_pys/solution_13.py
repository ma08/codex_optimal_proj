from math import *

h, v = map(int, input().split())
print(ceil(h/sin(radians(v))))
