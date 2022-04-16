

from sys import stdin
from math import ceil, sin, radians

h, v = [int(i) for i in stdin.readline().split()]

print(ceil(h/sin(radians(v))))
