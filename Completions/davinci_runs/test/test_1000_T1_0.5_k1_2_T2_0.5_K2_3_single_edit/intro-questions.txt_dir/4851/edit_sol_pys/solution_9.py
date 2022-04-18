#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline().strip())

while n != 0:
    n += 1
    sum_digits = 0
    for digit in str(n):
        sum_digits += int(digit)
    if n % sum_digits == 0:
        break

print(n)
