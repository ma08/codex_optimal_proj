
# SOLUTION

import sys
import math

num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    if a == b:  # if two numbers are equal
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
