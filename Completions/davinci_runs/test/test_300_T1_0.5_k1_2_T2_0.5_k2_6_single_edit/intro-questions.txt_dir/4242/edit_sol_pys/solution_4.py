
import math

A, B, K = map(int, input().split())

def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0: 
            factors.append(i) 
            n = n / i
        i = i + 1
    if n > 1:
        factors.append(n)
    return factors

def find_num(A, B, K):
    A_factors = prime_factorization(A)
    B_factors = prime_factorization(B)
    common_factors = list(set(A_factors) & set(B_factors))
    return int(common_factors[-K])

print(find_num(A, B, K))
