
import math

A, B, K = map(int, input().split())

def prime_factorization(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1): #2からnの平方根まで繰り返す
        while n % i == 0:
            n //= i #割り切れる間は割り続ける
            factors.append(i) #素因数を配列に入れる
    return factors

def find_num(A, B, K):
    a_factors = prime_factorization(A)
    b_factors = prime_factorization(B)
    common_factors = list(set(a_factors) & set(b_factors)) #共通の素因数を求める
    return common_factors[-K] #K番目に大きい素因数

print(find_num(A, B, K))
