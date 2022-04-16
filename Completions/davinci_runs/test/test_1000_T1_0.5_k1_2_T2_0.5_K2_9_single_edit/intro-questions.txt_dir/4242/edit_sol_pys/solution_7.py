import math

A, B, K = map(int, input().split())

def prime_factorization(A, B):
    A_factors = []
    B_factors = []
    for i in range(2, int(math.sqrt(A)) + 1):
        while A % i == 0:
            A //= i
            A_factors.append(i)
    for j in range(2, int(math.sqrt(B)) + 1):
        while B % j == 0:
            B //= j
            B_factors.append(j)
    return A_factors, B_factors

def find_num(A, B, K):
    A_factors, B_factors = prime_factorization(A, B)
    common_factors = list(set(A_factors) & set(B_factors))
    return common_factors[-K]

print(find_num(A, B, K))
