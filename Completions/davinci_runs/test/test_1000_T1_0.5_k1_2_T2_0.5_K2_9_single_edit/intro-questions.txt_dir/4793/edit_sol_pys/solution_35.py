
import sys
import math

s, v1, v2 = [int(i) for i in input().split()]

if s % v2 == 0:
    print(0, s // v2, end=" ")
elif s % v1 == 0:
    print(s // v1, 0, end=" ")
elif s < v1:
    print(1, 0, end=" ")
else:
    x = s // v1
    y = s % v1 // v2
    while s % v1 != 0 and s % v1 < v2:
        x -= 1
        y = s % v1 // v2
    if s % v1 != 0:
        print(x, y + 1, end=" ")
    else:
        print(x, y, end=" ")
