
import math

A, B, K = map(int, input().split())

def prime_factorization(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

A_factors = prime_factorization(A)
B_factors = prime_factorization(B)
common_factors = list(set(A_factors) & set(B_factors))
print(common_factors[-K])
