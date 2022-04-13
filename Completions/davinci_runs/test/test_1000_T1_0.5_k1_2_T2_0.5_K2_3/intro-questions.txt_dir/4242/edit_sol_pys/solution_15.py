
import math

A, B, K = map(int, input().split())

def prime_factorization(n): # 素因数分解
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

def find_num(A, B, K): # K番目に大きい約数を探す
    A_factors = prime_factorization(A)
    B_factors = prime_factorization(B)
    common_factors = list(set(A_factors) & set(B_factors))
    if len(common_factors) < K:
        return 0
    return common_factors[-K]

print(find_num(A, B, K))
