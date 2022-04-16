

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factorization(n):
    primes = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime(i) and n % i == 0:
            primes.append(i)
    return primes


print(prime_factorization(10))
