import math


def prime_factorization(num):
    factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num //= i
            factors.append(i)
    return factors


def find_num(A, B, K):
    A_factors = prime_factorization(A)
    B_factors = prime_factorization(B)
    common_factors = list(set(A_factors) & set(B_factors))
    return common_factors[-K]

print(find_num(A, B, K))
