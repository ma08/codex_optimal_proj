import sys
import heapq
from collections import deque
from itertools import combinations, permutations, combinations_with_replacement
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip() 

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass


n, m = map(int, input().split())
a = deque(map(int, input().split()))

if max(a) > n:
    print(-1)
    exit()

s = sum(a)
if s < n:
    print(n - s)
else:
    a.sort()
    s = 0
    for i in range(m):
        s += a[i]

    print(n - s)
