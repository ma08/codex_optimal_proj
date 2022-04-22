import math

A, B, K = map(int, input().split())

def prime_factorisation(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1): # sqrt(n)まででいい
        while n % i == 0:
            n //= i
            factors.append(i)
    if n != 1:
        factors.append(n)
    return factors

def find_num(A, B, K):
    A_factors = prime_factorisation(A) # Aの素因数分解
    B_factors = prime_factorisation(B) # Bの素因数分解
    common_factors = list(set(A_factors) & set(B_factors)) # A, Bの約数
    return common_factors[-K] # K番目に大きい約数

print(find_num(A, B, K))
