

import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def get_primes(num):
    primes = []
    for i in range(2, num + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def get_prime_factors(num):
    prime_factors = []
    # Get the primes that are less than or equal to num
    primes = get_primes(num)
    for prime in primes:
        if num % prime == 0:
            prime_factors.append(prime)
    return prime_factors

def main():
    num = int(input())
    print(get_prime_factors(num))

if __name__ == "__main__":
    main()
