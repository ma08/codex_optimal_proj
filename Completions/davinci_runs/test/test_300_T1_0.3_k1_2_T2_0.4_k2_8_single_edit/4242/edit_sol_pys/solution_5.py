#!/usr/bin/env python3

import sys

# Read input
a, b, k = map(int, sys.stdin.readline().split())

# Find all divisors of a and b
divisors_a = []
divisors_b = []
for i in range(1, a + 1):
    if a % i == 0:
        divisors_a.append(i)
for i in range(1, b + 1):
    if b % i == 0:
        divisors_b.append(i)

# Find the intersection of divisors_a and divisors_b
divisors = []
for i in divisors_a:
    if i in divisors_b:
        divisors.append(i)

# Find the k-th largest divisor
divisors.sort(reverse=True)
print(divisors[k - 1])
