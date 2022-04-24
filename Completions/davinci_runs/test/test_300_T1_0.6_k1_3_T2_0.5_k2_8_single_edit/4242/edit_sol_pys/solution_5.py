#!/bin/python3

import sys


# ============
# Solution
# ============

def gcd(a, b):
    a_prime, b_prime = a, b

    while a_prime != 0:
        a_prime, b_prime = b_prime % a_prime, a_prime

while a_prime != 0:
    a_prime, b_prime = b_prime % a_prime, a_prime

# The k-th largest number is a_prime / k
print(int(b_prime / k))
