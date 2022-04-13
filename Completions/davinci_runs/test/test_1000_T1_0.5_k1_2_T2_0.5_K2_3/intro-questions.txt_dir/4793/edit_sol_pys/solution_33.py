import sys
import math

s, v1, v2 = [int(i) for i in sys.stdin.readline().split()]

if s % v2 == 0:
    print(0, s // v2)
elif s % v1 == 0:
    print(s // v1, 0)
elif s < v1:
    print(1, 0)
else:
    x = s // v1
    y = s % v1 // v2
    while s % v1 != 0 and s % v1 < v2 and x >= 0:
        x -= 1
        y = s % v1 // v2
    if s % v1 != 0:
        print(x, y + 1)
    else:
        print(x, y)
