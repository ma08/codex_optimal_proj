
import sys
import math

a, b, c = map(int, input().split())
if b * b - 4 * a * c < 0:
    print('No')
else:
    print('Yes')
