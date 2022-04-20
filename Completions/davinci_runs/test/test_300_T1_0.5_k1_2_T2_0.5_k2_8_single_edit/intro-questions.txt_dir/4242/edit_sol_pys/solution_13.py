
import math

A, B, K = map(int, input().split())

def find_prime_factors(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

def find_num(A, B, K):
    A_factors = find_prime_factors(A)
    B_factors = find_prime_factors(B)
    common_factors = list(set(A_factors) & set(B_factors)) # list(set(A_factors).intersection(set(B_factors)))
    return common_factors[-K]

print(find_num(A, B, K))
