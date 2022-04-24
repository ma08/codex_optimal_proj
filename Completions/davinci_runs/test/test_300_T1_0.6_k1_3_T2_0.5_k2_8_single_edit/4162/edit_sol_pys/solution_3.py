import sys
from math import gcd
from functools import reduce
from functools import lru_cache
sys.setrecursionlimit(10**7)

N = int(input())
A = tuple(map(int, input().split()))



def lcmm(*args):
    return reduce(lcm, args)


def lcm(x, y):
    return x * y // gcd(x, y)


@lru_cache(maxsize=None)
def f(m):
    return sum((m - 1) % a + 1 for a in A)


l = lcmm(*A)
print(f(l))
