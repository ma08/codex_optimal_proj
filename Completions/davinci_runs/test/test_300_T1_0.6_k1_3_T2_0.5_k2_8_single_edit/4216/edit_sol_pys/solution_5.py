
import sys
sys.setrecursionlimit(1000000)
import math

n = int(input())

primes = []
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        primes.append(i)
        print(i)
        break
