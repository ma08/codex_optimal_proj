import sys
import math

n = int(input())

for i in range(n):
    x = int(input())
    if x == 0:
        print(1)
    else:
        print(int(math.factorial(x) % 10))
