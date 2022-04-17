# -*- coding: utf-8 -*-
import sys
import io
import numpy as np
import math
from collections import Counter
from collections import deque
from collections import defaultdict
from heapq import heappush, heappop
from itertools import accumulate
import fractions
from functools import reduce
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')
# pypyではinputは標準入力
# pypyではsys.stdin.readlineはinput
# pypyではsys.setrecursionlimitは10**7



def main():
    K = int(input())
    S = input()

    if len(S) > K:
        print(S[:K] + '...')
    else:
        print(S)


if __name__ == '__main__':
    main()
