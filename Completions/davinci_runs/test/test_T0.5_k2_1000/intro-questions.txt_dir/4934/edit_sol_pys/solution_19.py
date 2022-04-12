import math, sys

h, v = map(int, sys.stdin.readline().split())

print(math.ceil(h / math.sin(math.radians(v))))
