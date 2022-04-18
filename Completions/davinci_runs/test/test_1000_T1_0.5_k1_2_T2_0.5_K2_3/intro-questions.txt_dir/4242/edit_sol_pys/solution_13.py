import math

A, B, K = map(int, input().split())

def prime_factorization(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1): # 平方根まで考えれば良い
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors

def find_num(A, B, K):
    A_factors = prime_factorization(A)
    B_factors = prime_factorization(B)
    common_factors = list(set(A_factors) & set(B_factors))
    return common_factors[-K] # 一番大きい数からK番目の数を返す

print(find_num(A, B, K))
