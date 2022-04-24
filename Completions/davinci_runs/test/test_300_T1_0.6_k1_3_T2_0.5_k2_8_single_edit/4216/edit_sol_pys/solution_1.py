
import math

n = int(input())

primes = []
for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        primes.append(i)

print(n // primes[0])
