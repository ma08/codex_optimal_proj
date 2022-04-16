
import math


def is_prime(n):
    for i in range(2, math.floor(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

from itertools import combinations_with_replacement

n = int(input())

primes = []

for i in range(2, n):
    if is_prime(i):
        primes.append(i)

for i in primes:
    if n - i in primes:
        print(i, n - i)
        break
