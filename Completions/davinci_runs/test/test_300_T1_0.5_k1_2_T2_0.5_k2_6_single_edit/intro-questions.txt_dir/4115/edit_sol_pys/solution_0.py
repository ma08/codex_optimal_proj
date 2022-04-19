import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7


def sol():
    s = input().strip()

    if s == s[::-1]:
        print(0)
        exit()

for i in range(len(s) // 2):
    if s[i] == s[-1 - i]:
        continue
    else:
        print(1)
        break
else:
    print(1)
