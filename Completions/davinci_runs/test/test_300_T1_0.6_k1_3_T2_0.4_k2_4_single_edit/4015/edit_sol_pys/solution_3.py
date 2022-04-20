

import sys
import math as m

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_semiprime(n):
    if n == 1:
        return False
    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i) and is_prime(n / i):
                return True
    return False

def is_almost_prime(n):
    if n == 1:
        return False
    count = 0
    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if count > 1:
                return False
    if count == 1:
        return True
    return False

n = int(sys.stdin.read())

count = 0
for i in range(1, n + 1):
    if is_almost_prime(i):
        count += 1

print(count)
