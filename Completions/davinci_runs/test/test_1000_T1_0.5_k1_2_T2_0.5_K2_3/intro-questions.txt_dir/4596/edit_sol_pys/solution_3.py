import sys
import math
from collections import deque, defaultdict, Counter
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

n = int(input())
a = [int(x) for x in input().split()]

count = 0
while all(x % 2 == 0 for x in a):
    a = [x // 2 for x in a]
    count += 1

print(count)

def main():
    pass

if __name__ == '__main__':
    main()
