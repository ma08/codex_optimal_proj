

# SOLUTION
# This is a small variation of the problem "Almost Prime Numbers"
# https://codeforces.com/contest/1148/problem/C

# The idea is to find the prime factors of the number x.
# For that, we must find the largest prime factor of the product of all the divisors
# We will use the sieve of Eratosthenes

# This is a variation of the problem "Almost Prime Numbers"
# https://codeforces.com/contest/1148/problem/C

# The idea is to find the prime factors of the number x.
# For that, we must find the largest prime factor of the product of all the divisors
# We will use the sieve of Eratosthenes

# The algorithm will be as follows:
# 1. We will find the product of all the divisors
# 2. We will use the sieve of Eratosthenes to find the largest prime factor of the product
# 3. We will divide the product by the largest prime factor and repeat the process until it is 1
# 4. We will multiply all the prime factors

# This algorithm is O(n log log n)

# If the product is 1, then the divisors are not divisors of any number
# If the product is not 1 and we cannot find any prime factor, then the divisors are the divisors of a prime number

import math

t = int(input())

def sieve(n):
    # We will use an array to represent the sieve
    # The value 0 means that the number is prime
    # The value 1 means that the number is not prime
    sieve = [0 for _ in range(n + 1)]
    sieve[0] = 1
    sieve[1] = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i] == 0:
            j = i * i
            while j <= n:
                sieve[j] = 1
                j += i
    return sieve

for _ in range(t):
    n = int(input())
    divisors = [int(x) for x in input().split()]
    product = 1
    for divisor in divisors:
        product *= divisor
    sieve = sieve(product)
    primes = []
    while product != 1:
        for i in range(product, 0, -1):
            if sieve[i] == 0:
                primes.append(i)
                product //= i
                break
        if product == 1:
            break
    if len(primes) == 0:
        print(-1)
    else:
        print(product * max(primes))