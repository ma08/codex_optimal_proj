

import math
import collections
import bisect
import sys
import copy
import fractions
import random
import string
import itertools
sys.setrecursionlimit(10 ** 9)
mod = 10 ** 9 + 7
inf = 10 ** 19

N, D = map(int, input().split())

def main():
    if N <= D:
        print(1)
    else:
        print(math.ceil((N - D) / (2 * D + 1)) + 1)

main()
