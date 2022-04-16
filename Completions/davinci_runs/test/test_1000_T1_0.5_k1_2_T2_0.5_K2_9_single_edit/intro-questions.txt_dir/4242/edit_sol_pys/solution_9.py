import math


def prime_factorization(num):
    factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num //= i
            factors.append(i)
    return factors


print(find_num(A, B, K))
