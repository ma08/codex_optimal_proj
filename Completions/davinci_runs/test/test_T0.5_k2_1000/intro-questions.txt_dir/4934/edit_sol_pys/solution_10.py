import sys
import math

h, v = map(float, sys.stdin.readline().split())

print(math.ceil(h / math.sin(math.radians(v))))
