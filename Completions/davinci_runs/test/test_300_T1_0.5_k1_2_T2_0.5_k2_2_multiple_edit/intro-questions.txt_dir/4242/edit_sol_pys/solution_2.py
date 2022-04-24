
import math

A, B, K = map(int, input().split())

def prime_factorization(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

def find_num(A, B, K):
    a_factors = prime_factorization(A)
    b_factors = prime_factorization(B)
    common_factors = list(set(a_factors) & set(b_factors))
    return common_factors[-1]

print(find_num(A, B, K))
