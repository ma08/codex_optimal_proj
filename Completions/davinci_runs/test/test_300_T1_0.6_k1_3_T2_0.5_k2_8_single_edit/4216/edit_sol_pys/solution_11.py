
import math

def factor(n):
    primes = []
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            primes.append(i)
    return primes

if __name__ == "__main__":
    n = int(input())
    print(n // factor(n)[0])
