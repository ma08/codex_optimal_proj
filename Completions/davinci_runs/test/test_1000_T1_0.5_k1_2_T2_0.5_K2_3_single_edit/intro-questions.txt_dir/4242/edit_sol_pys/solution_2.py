
import math

A, B, K = map(int, input().split())

def prime_factorization(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            factors.append(i)
    if n != 1:
        factors.append(n)
    return factors

def find_num(A, B, K):
    A_factors = prime_factorization(A)
    B_factors = prime_factorization(B)
    common_factors = list(set(A_factors) & set(B_factors))
    return common_factors[K - 1]

print(find_num(A, B, K))
