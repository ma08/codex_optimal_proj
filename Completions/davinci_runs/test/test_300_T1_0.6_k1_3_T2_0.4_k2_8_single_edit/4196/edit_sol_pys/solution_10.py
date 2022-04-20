#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

import sys


def gcd(a, b): return a if b == 0 else gcd(b, a % b)


# N (2 <= N <= 10^5)
n = int(sys.stdin.readline())


# A_1, A_2, ..., A_N (1 <= A_i <= 10^9)
a = [int(i) for i in sys.stdin.readline().strip().split()]

# Find the maximum possible greatest common divisor of the N integers on the blackboard after your move.
max_gcd = 0
for i in range(n):
  for j in range(i + 1, n):
    max_gcd = max(max_gcd, gcd(a[i], a[j]))

print(max_gcd)
