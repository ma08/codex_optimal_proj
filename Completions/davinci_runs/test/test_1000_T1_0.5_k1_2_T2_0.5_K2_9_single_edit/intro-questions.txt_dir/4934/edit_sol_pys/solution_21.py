#!/usr/bin/env python3

from math import *

h, v = map(int, input().split())
print(ceil(h/sin(radians(v))))
