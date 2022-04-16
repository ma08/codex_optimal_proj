# -*- coding: utf-8 -*-

from math import *

h, v = map(int, input().split())
print(ceil(h/sin(radians(v)))) # print(h/sin(radians(v)) + 1)
