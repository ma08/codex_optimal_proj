# -*- coding: utf-8 -*-

import itertools
from collections import defaultdict
import sys

def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b = list(map(int, sys.stdin.readline().split()))
    b.sort()
    c = list(map(int, sys.stdin.readline().split()))
    c.sort()
    d = defaultdict(list)
    for i, j in itertools.product(b, c):
        d[i + j].append((i, j))
    for k, v in d.items():
        print(k, v)
    # for i in a:
    #     for j in d[-i]:
    #         print(i, j[0], j[1])




if __name__ == '__main__':
    main()
