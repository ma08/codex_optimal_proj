
from math import gcd, ceil
from functools import reduce

N = int(input())
A = tuple(map(int, input().split()))


def lcm(x, y):
    return x * y // gcd(x, y)


def lcmm(*args):
    return reduce(lcm, args)


def f(m):
    return sum(ceil(m / a) for a in A)


l = lcmm(*A)
print(f(l))
