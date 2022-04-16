
import sys
import math

h, v = map(int, sys.stdin.readline().split())

print(int(math.ceil(h / math.sin(math.radians(v)))))
