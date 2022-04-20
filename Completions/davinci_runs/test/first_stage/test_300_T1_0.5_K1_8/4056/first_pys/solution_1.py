

import functools
import operator
import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

n = int(input())
a = list(map(int, input().split()))

print(functools.reduce(lambda x, y: gcd(x, y), a))