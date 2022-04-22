import math


def eratosthenes(n):
    l = [True] * (n + 1)
    l[0] = False
    l[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if not l[i]:
            continue
        for j in range(i * 2, n + 1, i):
            l[j] = False
    return [i for i in range(n + 1) if l[i]]

def get_divisor(n):
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res

N = int(input())

primes = eratosthenes(55555)

for p in primes:
    if N % p == 0:
        print(p)
        exit()
