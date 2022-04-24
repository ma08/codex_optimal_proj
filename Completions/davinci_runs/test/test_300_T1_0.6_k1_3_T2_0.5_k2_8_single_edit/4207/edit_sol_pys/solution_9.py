from collections import deque
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from functools import lru_cache
from heapq import heappush, heappop
from itertools import permutations, combinations
from itertools import accumulate
from itertools import product
from itertools import combinations_with_replacement
from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right
from math import gcd, floor, ceil
from math import sqrt
import sys
sys.setrecursionlimit(10**9)
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7

import random

#for i in range(100):
#    n = random.randint(1, 200000)
#    a = [random.randint(-1000000000, 1000000000) for i in range(n)]
#    b = [random.randint(-1000000000, 1000000000) for i in range(n)]
#    print(n)
#    print(' '.join(map(str, a)))
#    print(' '.join(map(str, b)))

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def solve(n, a, b):
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    if a[0] == 0:
        return n
    if a[0] < 0:
        a = list(map(lambda x: -x, a))
        b = list(map(lambda x: -x, b))
    if b[0] > 0:
        return 0
    if b[n-1] < 0:
        return n
    if a[0] == a[n-1]:
        if a[0] == 0:
            return n
        return n - (b[-1] - b[0]) // a[0]
    return max(n - (b[-1] - b[0]) // a[0], n - (b[-1] - b[0]) // a[n-1])

print(solve(n, a, b))
