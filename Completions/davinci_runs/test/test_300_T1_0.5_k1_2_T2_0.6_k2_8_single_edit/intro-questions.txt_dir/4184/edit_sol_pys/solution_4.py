import sys
import math

sys.setrecursionlimit(1000000000)

def read_ints():
    return list(map(int, input().split(' ')))


def read_int():
    return int(input())


def read_str():
    return input()


def read_str_list():
    return input().split(' ')



N = int(input())
W = list(map(int, input().split()))

min_diff = 100 * N
for t in range(1, N):
    s1 = sum(W[:t])
    s2 = sum(W[t:])
    diff = abs(s1 - s2)
    if diff < min_diff:
        min_diff = diff



def solve():
    pass


solve()
print(min_diff)
