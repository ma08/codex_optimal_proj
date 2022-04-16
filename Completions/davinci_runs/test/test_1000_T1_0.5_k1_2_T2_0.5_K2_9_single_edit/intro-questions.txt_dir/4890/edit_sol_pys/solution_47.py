

import sys


def get_neighbors(n, m, s, d, c):
    return []

import random

def solve(n, m, s, d, c):
    # Write your code here
    # return a list of length s with your solution
    return [0] * s


lines = sys.stdin.readlines()
n, m, s, d = [int(x) for x in lines[0].split()]
c = [int(x) for x in lines[1].split()]
neighbors = get_neighbors(n, m, s, d, c)


res = solve(n, m, s, d, c)

if res is None:
    print("impossible")
else:
    print(" ".join([str(x) for x in res]))
