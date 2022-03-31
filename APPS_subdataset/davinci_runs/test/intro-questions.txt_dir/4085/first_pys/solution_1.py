

import sys

def get_primes(n):
    """
    Gets all primes less than n
    """
    primes = [2]
    for i in range(3, n+1, 2):
        is_prime = True
        for j in range(3, i, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def get_factors(n, primes):
    """
    Gets all factors of n
    """
    factors = []
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors

def get_divisors(n, primes):
    """
    Gets all divisors of n
    """
    factors = get_factors(n, primes)
    n_factors = len(factors)
    divisors = set([1, n])
    for i in range(1 << n_factors):
        divisor = 1
        for j in range(n_factors):
            if i & 1 << j:
                divisor *= factors[j]
        divisors.add(divisor)
    return divisors

def get_missing_divisors(divisors, n):
    """
    Gets all divisors of n that are not in divisors
    """
    missing = set(divisors) - set(n)
    missing.remove(1)
    return missing

def get_number_from_divisors(divisors):
    """
    Gets the smallest number that has divisors as its divisors
    """
    primes = get_primes(max(divisors))
    for d in divisors:
        missing = get_missing_divisors(get_divisors(d, primes), divisors)
        if len(missing) == 1:
            return d * missing.pop()
    return -1
    
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    divisors = [int(x) for x in sys.stdin.readline().split()]
    print(get_number_from_divisors(divisors))