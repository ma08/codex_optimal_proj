import math

import sys

n = int(input())

h = list(map(int, input().split()))

diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
