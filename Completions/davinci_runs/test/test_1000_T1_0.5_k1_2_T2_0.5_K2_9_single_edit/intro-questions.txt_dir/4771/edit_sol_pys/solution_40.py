

import sys
from math import pow

n = int(sys.stdin.readline())
V = int(sys.stdin.readline())

max_volume = 0

for i in range(n):
    l, w, h = [int(j) for j in sys.stdin.readline().split()]
    max_volume = max(max_volume, l*w*h)

print(max_volume-V)
