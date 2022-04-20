

import math


def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


N = int(input())  # N!
divisors = get_divisors(N)
divisors.sort()

for i in range(len(divisors)):
    if divisors[i] != 1 and divisors[i] != N:
        print(divisors[i])
        break
