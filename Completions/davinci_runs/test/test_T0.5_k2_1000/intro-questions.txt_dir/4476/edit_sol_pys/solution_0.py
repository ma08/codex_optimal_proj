
# SOLUTION 

import sys
import math
t = int(input())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        print(0)
    else:
        if a % 2 == 1:
            if b % 2 == 1:
                print(int(math.ceil(abs(a - b) / 2)))
            else:
                print(int(math.ceil(abs(a - b) / 2)) + 1)
        else:
            if b % 2 == 1:
                print(int(math.ceil(abs(a - b) / 2)) + 1)
            else:
                print(int(math.ceil(abs(a - b) / 2)))
