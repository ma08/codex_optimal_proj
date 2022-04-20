
from math import gcd
from functools import reduce
from functools import lru_cache as cache

N = int(input())
A = tuple(map(int, input().split()))


def lcm(x, y):
    return x * y // gcd(x, y)


def lcmm(*args):
    return reduce(lcm, args)


@cache(maxsize=None)
def f(m):
    return sum(m % a for a in A)


l = lcmm(*A)
print(f(l))
