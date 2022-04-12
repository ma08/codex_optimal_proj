import math

A, B, K = map(int, input().split())

def prime_factorisation(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

def find_num(A, B, K):
    A_factors = prime_factorisation(A)
    B_factors = prime_factorisation(B)
    common_factors = list(set(A_factors) & set(B_factors))
    return common_factors[-K] if len(common_factors) >= K else 1

print(find_num(A, B, K))
