
import sys
import math
from collections import deque
from collections import Counter
from functools import reduce

sys.setrecursionlimit(10**7)
f_inf = float('inf')
mod = 10**9 + 7

def gcd(a, b):
    if(a < b):
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def dfs(s, n):
    if s > 9:
        return 0
    if n == 1:
        return 1
    res = dfs(s + 1, n - 1) + dfs(s, n - 1)
    return res % MOD


def solve():
    return dfs(0, N - 1) * 2 % MOD


print(solve())
