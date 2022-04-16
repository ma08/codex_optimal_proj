# write a program that calculates the minimum number of bricks needed to reach the top of a building

from math import *

h, v = map(int, input().split())
print(ceil(h/sin(radians(v))))
