import sys, math

N = int(sys.stdin.readline())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for i in range(1, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def main():
    primes = get_primes(N)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] + primes[j] + primes[k] == N:
                    print(primes[i], primes[j], primes[k])
                    return
    print(0)

main()
