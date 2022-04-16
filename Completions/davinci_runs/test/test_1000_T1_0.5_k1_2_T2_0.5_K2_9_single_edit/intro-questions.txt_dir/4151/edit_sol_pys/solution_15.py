#! /usr/bin/env python3

from collections import Counter


import sys

def main():
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    assert 2 <= n <= 2 * 10**5
    assert len(A) == n
    assert all(1 <= x <= 10**9 for x in A)

    c = Counter(A)
    print(len(c))
    # TODO: solve the problem


if __name__ == '__main__':
    main()
