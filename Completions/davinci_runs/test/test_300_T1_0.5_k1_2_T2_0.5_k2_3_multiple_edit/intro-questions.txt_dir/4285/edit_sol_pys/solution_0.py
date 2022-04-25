
import collections
import sys, re
import math
from collections import defaultdict
from collections import deque
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product
from itertools import accumulate
from operator import itemgetter
from functools import reduce
from bisect import bisect_left
from bisect import bisect_right
from bisect import bisect
from heapq import heappop
from heapq import heappush
from heapq import heapify
from queue import deque
from math import ceil
from math import floor
from math import sqrt
from copy import deepcopy
import numpy as np
import scipy as sp
import math
import sys
sys.setrecursionlimit(10**9)
mod = 10**9+7
INF = 10**19
# input = sys.stdin.readline
def inp(): return int(input())
def inp_list(): return list(map(int, input().split()))
def lcm(x, y): return (x * y) // math.gcd(x, y)
def lcm_list(nums): return reduce(lcm, nums, 1)
def gcd_list(nums): return reduce(gcd, nums, nums[0])
def gcd(x, y): return math.gcd(x, y)
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
def lcm(a,b): return (a*b)/gcd(a,b)
sys.setrecursionlimit(10**6)
 
S = input()
 
 
def main():
    for i in range(len(S)):
        if S[i] == '?':
            if S[i-1] == 'P':
                S = S[:i] + 'D' + S[i+1:]
            elif S[i-1] == 'D':
                S = S[:i] + 'P' + S[i+1:]
            else:
                S = S[:i] + 'D' + S[i+1:]
    print(S)
 
if __name__ == '__main__':
    main()
