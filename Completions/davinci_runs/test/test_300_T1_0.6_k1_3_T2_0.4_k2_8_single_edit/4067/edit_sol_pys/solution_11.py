#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]



def main():
    n = int(input())
    s = input()
    d = {'0': 0, '1': 0, '2': 0}
    for c in s:
        d[c] += 1
    if d['1'] < d['2']:
        d['1'] += 1
        d['2'] -= 1
    elif d['1'] > d['2']:
        d['1'] -= 1
        d['2'] += 1
    print('0' * d['0'] + '1' * d['1'] + '2' * d['2'])


if __name__ == '__main__':
    main()
