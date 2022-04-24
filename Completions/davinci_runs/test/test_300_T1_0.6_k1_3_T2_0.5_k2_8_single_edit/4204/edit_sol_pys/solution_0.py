
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = [2]
    for i in range(3,n+1,2):
        if is_prime(i):
            primes.append(i)
    return primes

print(get_primes(int(input())))
