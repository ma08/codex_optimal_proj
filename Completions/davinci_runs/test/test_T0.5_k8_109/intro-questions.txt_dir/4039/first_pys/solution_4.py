

from collections import deque
from collections import defaultdict
from collections import Counter
from itertools import permutations
from itertools import combinations
from collections import OrderedDict
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import ceil
from math import inf
import sys

sys.setrecursionlimit(500000)


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]


n, r = LI()
p = LIR(n)

for i in range(n):
    r -= p[i][0]
    if r < 0:
        print('NO')
        exit()
    r += p[i][1]

print('YES')