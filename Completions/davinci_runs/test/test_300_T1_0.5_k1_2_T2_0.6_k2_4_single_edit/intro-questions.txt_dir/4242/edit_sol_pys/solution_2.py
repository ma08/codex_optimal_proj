import math

A, B, K = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = []
    for i in range(n):
        if is_prime(i) == True:
            primes.append(i)
    return primes

def find_num(a, b, k):
    primes = prime_numbers(100)
    primes_a = []
    primes_b = []
    for p in primes:
        if a % p == 0:
            primes_a.append(p)
        if b % p == 0:
            primes_b.append(p)
    common_primes = list(set(primes_a) & set(primes_b))
    return common_primes[-k]

print(find_num(A, B, K)) 
