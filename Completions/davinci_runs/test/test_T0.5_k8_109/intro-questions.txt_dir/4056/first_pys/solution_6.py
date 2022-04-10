

import sys
import math

def get_primes(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def factorize(n, primes):
    factors = []
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            factors.append(p)
    return factors

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    primes = get_primes(int(math.sqrt(max(a))))
    factors = [factorize(x, primes) for x in a]
    lcm_factors = []
    for f in factors:
        lcm_factors.append(f[0])
        for i in range(1, len(f)):
            lcm_factors[-1] = lcm(lcm_factors[-1], f[i])
    answer = 1
    for f in lcm_factors:
        answer *= f
    print(answer)

if __name__ == '__main__':
    main()