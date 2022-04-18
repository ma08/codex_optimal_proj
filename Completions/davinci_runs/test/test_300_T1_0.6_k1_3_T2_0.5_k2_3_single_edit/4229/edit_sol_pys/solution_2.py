import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N = int(input())

    # 3の倍数と5の倍数を数える
    c3 = (N-1)//3
    c5 = (N-1)//5
    c15 = (N-1)//15

    # 3の倍数と5の倍数を引いて、それぞれ足す
    print(3*c3*(c3+1)//2 + 5*c5*(c5+1)//2 - 15*c15*(c15+1)//2)


sol()
