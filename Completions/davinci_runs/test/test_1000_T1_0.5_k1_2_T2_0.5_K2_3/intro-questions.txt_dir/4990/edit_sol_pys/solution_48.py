import sys
import math

b, k, g = map(float, sys.stdin.readline().split())
print(math.ceil(b / g))
