import sys
import math
from itertools import permutations
from itertools import combinations
from itertools import product
from collections import deque
from collections import Counter

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


sys.setrecursionlimit(1000000)


n, a, b = map(int, input().split())

def sum_of_digits(n):
    return sum([int(i) for i in str(n)])

res = 0
for i in range(1, n+1):
    if a <= sum_of_digits(i) <= b:
        res += i

print(res)
