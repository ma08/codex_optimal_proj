

import sys
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 2
    return primes

def get_a(b, n):
    a = []
    primes = get_primes(len(b))
    for i in range(n):
        if b[i] in primes:
            a.append(primes.index(b[i]) + 2)
        else:
            for j in range(2, b[i] // 2 + 1):
                if b[i] % j == 0:
                    a.append(j)
                    break
    return a

def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    a = get_a(b, n)
    print(*a)

if __name__ == "__main__":
    main()