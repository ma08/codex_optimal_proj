
from math import *

h, v = map(float, input().split())
print(int(ceil(h/sin(radians(v)))))
