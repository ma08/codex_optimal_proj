#!/usr/bin/env python3

import sys

def check_prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))
