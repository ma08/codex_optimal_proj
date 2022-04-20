import math

A, B, K = map(int, input().split())  # A, B, K = 4, 10, 3

def prime_factorization(n):
    factors = []  # factors = [2, 2]
    for i in range(2, int(math.sqrt(n)) + 1):  # i = 2, 3, 4
        while n % i == 0:  # n = 4, 2, 1
            n //= i  # n = 2, 1
            factors.append(i)  # factors = [2, 2]
    return factors  # factors = [2, 2]

def find_num(A, B, K):
    A_factors = prime_factorization(A)  # A_factors = [2, 2]
    B_factors = prime_factorization(B)  # B_factors = [2, 5]
    common_factors = list(set(A_factors) & set(B_factors))  # common_factors = [2]
    return common_factors[-K]  # return 2

print(find_num(A, B, K))
