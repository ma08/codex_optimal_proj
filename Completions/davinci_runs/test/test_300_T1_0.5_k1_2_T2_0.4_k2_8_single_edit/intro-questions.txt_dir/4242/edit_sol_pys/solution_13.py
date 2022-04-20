import math

A, B, K = map(int, input().split())

def find_num(A, B, K):
    for i in range(max(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            K -= 1
        if K == 0:
            return i

def find_num(A, B, K):
    A_factors = prime_factorization(A)
    B_factors = prime_factorization(B)
    common_factors = list(set(A_factors) & set(B_factors))
    return common_factors[-K]

print(find_num(A, B, K))
