import math

A, B, K = map(int, input().split())

def prime_factorization(n, is_prime):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1): #素数の場合は2からn-1まで
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

def find_num(A, B, K, is_prime):
    A_factors = prime_factorization(A, is_prime)
    B_factors = prime_factorization(B, is_prime)
    common_factors = list(set(A_factors) & set(B_factors))
    if len(common_factors) < K:
        return -1
    return common_factors[-K]

if A == 1 or B == 1:
    is_prime = True
else:
    is_prime = False

print(find_num(A, B, K, is_prime))
