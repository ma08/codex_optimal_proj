

import sys

n = int(sys.stdin.readline())
heights = [int(x) for x in sys.stdin.readline().split()]

for i in range(1, n):
    if heights[i] < heights[i - 1]:
        heights[i] += 1

if sorted(heights) == heights:
    print('Yes')
else:
    print('No')