#!/usr/bin/env python3

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    assert 2 <= n <= 2 * 10 ** 5
    assert len(a) == n
    assert all(1 <= x <= 10 ** 9 for x in a)

    # TODO: solve the problem


if __name__ == '__main__':
    main()
