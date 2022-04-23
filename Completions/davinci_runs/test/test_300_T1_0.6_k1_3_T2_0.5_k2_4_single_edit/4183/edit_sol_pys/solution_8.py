
import itertools
import sys

def solve(n, m, a):
    perm = itertools.permutations(a)
    for p in perm:
        for i in range(n-1):
            if p[i] == p[i+1]:
                break
        else:
            return ' '.join(p)
    return -1
