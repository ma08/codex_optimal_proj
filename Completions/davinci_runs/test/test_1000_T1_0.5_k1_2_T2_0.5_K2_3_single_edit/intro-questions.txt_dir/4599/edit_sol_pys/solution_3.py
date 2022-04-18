import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7


def sol():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)

alice_sum = 0
bob_sum = 0

for i in range(N):
    if i % 2 == 0:
        alice_sum += A[i]
    else:
        bob_sum += A[i]

print(alice_sum - bob_sum)
