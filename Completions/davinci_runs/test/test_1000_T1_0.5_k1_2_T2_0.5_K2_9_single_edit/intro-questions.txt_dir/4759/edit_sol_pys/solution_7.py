

import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

# Calculate and print the slugging percentage
print(total_bases / valid_at_bats)
