#!/usr/bin/env python3
# this is a comment 
from math import *

h, v = map(int, input().split())
print(ceil(h/sin(radians(v))))
