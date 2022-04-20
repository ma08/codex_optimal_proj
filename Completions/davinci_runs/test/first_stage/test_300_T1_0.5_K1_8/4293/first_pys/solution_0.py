

import sys
import math

p, q, r = (int(x) for x in sys.stdin.readline().split())

print(min(p+q, q+r, r+p))