

import sys, math

N = int(sys.stdin.readline())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

num_of_primes = 0
for i in range(2, N + 1):
    if is_prime(i):
        num_of_primes += 1

print(num_of_primes)
