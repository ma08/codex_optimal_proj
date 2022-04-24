# -----Imports-----
import sys
import math
from fractions import gcd
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter, mul
from copy import copy, deepcopy
from functools import reduce
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import date
from decimal import Decimal
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

# -----Constants-----
MOD = 10 ** 9 + 7

# -----Functions-----


# -----Input and Output-----
[K] = [int(input()) for i in range(1)]

# -----Solve-----
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            ans += gcd(a, gcd(b, c))
print(ans % MOD)
