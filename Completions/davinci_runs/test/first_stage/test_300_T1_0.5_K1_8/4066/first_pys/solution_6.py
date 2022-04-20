

import sys
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def lcm_pair(a):
    min_lcm = sys.maxsize
    min_pair = None
    for i, ai in enumerate(a):
        for j, aj in enumerate(a[i+1:]):
            aj_ = aj + i + 1
            lcm_ = lcm(ai, aj)
            if lcm_ < min_lcm:
                min_lcm = lcm_
                min_pair = (i+1, aj_)
    return min_pair

n = int(input())
a = [int(i) for i in input().split()]

print(*lcm_pair(a))