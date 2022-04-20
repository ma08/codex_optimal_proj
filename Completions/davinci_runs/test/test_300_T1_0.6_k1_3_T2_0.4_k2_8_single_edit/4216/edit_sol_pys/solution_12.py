
import math

n = int(input())

primes = []
for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        n = n // i
        primes.append(i)

print(n // primes[0])
