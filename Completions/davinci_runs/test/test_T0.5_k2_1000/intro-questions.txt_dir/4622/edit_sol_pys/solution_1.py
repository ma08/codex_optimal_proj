import sys
import math

def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def main():
    n = int(sys.stdin.readline())
    primes = sieve(n)
    for i in range(n):
        print(i, primes[i])

if __name__ == "__main__":
    main()
