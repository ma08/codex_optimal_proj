import math

A, B, K = map(int, input().split()) # A = 10, B = 20, K = 2

def prime_factorisation(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1): # i = 2, 3, 4, 5, 6, 7, 8, 9, 10
        while n % i == 0:
            n //= i # n = 5, 2, 1
            factors.append(i)
    return factors # factors = [2, 5]

def find_num(A, B, K):
    A_factors = prime_factorisation(A) # A_factors = [2, 5]
    B_factors = prime_factorisation(B) # B_factors = [2, 5]
    common_factors = list(set(A_factors) & set(B_factors)) # common_factors = [2, 5]
    return common_factors[-K] # common_factors[-K] = [2, 5][-2] = [2, 5][1] = 5

print(find_num(A, B, K))
