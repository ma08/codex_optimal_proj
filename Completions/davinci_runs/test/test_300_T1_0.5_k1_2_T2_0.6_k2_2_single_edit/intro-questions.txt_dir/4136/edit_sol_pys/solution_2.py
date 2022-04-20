from collections import deque
from heapq import heappush, heappop
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
from fractions import gcd
import sys
import math

mod = 10**9+7
inf = float('inf')


def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ans = 0
    before = -1
    for i in range(n):
        ans += b[a[i]-1]
        if a[i]-1 == before+1:
            ans += c[before]
        before = a[i]-1
    print(ans)

main()
