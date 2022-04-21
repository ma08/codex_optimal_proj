

# Import
import sys
import bisect
from copy import deepcopy
from collections import *
from itertools import *
from functools import *

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7
import math

# Functions
def read(): return sys.stdin.readline().strip()
def read_list(t): return list(map(t, read().split()))
def read_line(t): return t(read())
def read_lines(t, N): return [t(read()) for _ in range(N)]

def main():
    N = read_line(int)
    d = read_list(int)

    # Sorting
    d.sort()

    # Number of problems
    count = 0

    # Solve
    for i in range(N//2):
        if d[i] == d[N//2]:
            count += 1
        elif d[i] < d[N//2]:
            break

    print(count)

# Main
if __name__ == "__main__":
    main()
