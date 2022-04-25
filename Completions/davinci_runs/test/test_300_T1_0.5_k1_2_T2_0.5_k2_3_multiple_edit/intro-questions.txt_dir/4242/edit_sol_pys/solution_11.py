import math

A, B, K = map(int, input().split())

def prime_factorisation(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

def find_num(n1, n2, k):
    n1_factors = prime_factorisation(n1)
    n2_factors = prime_factorisation(n2)
    common_factors = list(set(n1_factors) & set(n2_factors))
    return common_factors[-K]

print(find_num(A, B, K))
