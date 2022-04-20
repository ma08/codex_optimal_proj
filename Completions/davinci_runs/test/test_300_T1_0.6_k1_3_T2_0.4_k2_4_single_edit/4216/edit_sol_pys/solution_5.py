
import math

n = int(input())

primes = []
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        primes.append(i)

if len(primes) == 0:
    print(1)
else:
    print(n // primes[0])
