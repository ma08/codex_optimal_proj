#!/usr/bin/env python3

import sys
import math

def main():
    n = int(sys.stdin.readline())
    # find all prime factors
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        if n % i == 0:
            primes.append(i)
            n //= i
        else:
            i += 2
    if n != 1:
        primes.append(n)
    # count how many times each prime occurs
    counts = {}
    for p in primes:
        if p not in counts:
            counts[p] = 0
        counts[p] += 1
    # find the number of points
    k = 1
    for c in counts.values():
        k *= c+1
    print(k)

if __name__ == '__main__':
    main()
