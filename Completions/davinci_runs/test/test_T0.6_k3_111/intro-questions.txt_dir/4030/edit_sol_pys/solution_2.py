import sys
import os
import math
import random
import heapq 
import time
import copy
import itertools
from collections import deque
from functools import reduce
sys.setrecursionlimit(10**7)
inf = 10**10
mod = 10**9 + 7

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def main2():
    n = I()
    a = LI()
    a.sort()
    print(a[n//2])

def main():
    main2()


if __name__ == '__main__':
    main()
