#!/usr/bin/env python3

import sys, math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a,b)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt = int(math.sqrt(n)) + 1
    for i in range(3, sqrt, 2):
        if n % i == 0:
            return False
    return True

def find_prime(n):
    if is_prime(n):
        return n
    for i in range(n+1, n+10000):
        if is_prime(i):
            return i

def factorize(n):
    if is_prime(n):
        return [n]

    factors = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return factors

def find_factor(n):
    if is_prime(n):
        return n

    factors = factorize(n)
    for f in factors:
        if is_prime(f):
            return f

def main():
        n = int(line)
        print(i, find_prime(n))

    # for i, line in enumerate(lines[1:], 1):
    #     n = int(line)
    #     print(i, find_factor(n))

if __name__ == '__main__':
    main()
