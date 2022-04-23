

import sys
import math

a = int(input())
b = int(input())
c = int(input())

print(a + b + c - max(a, b, c) - min(a, b, c))
