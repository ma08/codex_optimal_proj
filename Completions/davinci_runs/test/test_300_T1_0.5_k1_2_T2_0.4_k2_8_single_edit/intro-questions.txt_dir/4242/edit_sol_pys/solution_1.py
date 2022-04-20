import math

A, B, K = map(int, input().split()) #A, B, Kを入力

def prime_factorization(n): #nを素因数分解する関数
    factors = [] #素因数を格納するリスト
    for i in range(2, int(math.sqrt(n)) + 1): #iが2から√nまで
        while n % i == 0: #nをiで割り切れる限り
            n //= i #nをiで割る
            factors.append(i) #iを素因数としてリストに追加
    return factors #素因数のリストを返す

def find_num(A, B, K):
    A_factors = prime_factorization(A)
    B_factors = prime_factorization(B)
    common_factors = list(set(A_factors) & set(B_factors))
    return common_factors[-K]

print(find_num(A, B, K))
