import math

A, B, K = map(int, input().split())

def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def find_num(A, B, K):
    A_factors = prime_factorization(A)
    B_factors = prime_factorization(B)
    common_factors = list(set(A_factors) & set(B_factors))
    return common_factors[-K]

print(find_num(A, B, K))
