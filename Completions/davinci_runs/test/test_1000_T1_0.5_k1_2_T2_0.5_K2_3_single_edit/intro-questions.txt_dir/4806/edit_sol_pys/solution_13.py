import sys
import math
from collections import deque
from functools import reduce
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808

def pow(x, y): return pow(x, y, M)

def pow(x, y, m):
    if y == 0: return 1
    a = pow(x, y//2, m)
    a = a * a % m
    if y % 2 == 1:
        a = a * x % m
    return a

def make_fact(n):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % M)
    return fact

def make_factinv(fact):
    inv = [1] * len(fact)
    inv[-1] = pow(fact[-1], M - 2, M)
    for i in range(len(fact) - 2, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % M
    return inv

def nCr(n, r, fact, inv):
    if n < r: return 0
    return fact[n] * inv[r] * inv[n-r] % M

def nPr(n, r, fact, inv):
    if n < r: return 0
    return fact[n] * inv[n-r] % M

def nHr(n, r, fact, inv):
    return nCr(n+r-1, r, fact, inv)

def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

def lcm(x, y): return x // gcd(x, y) * y

def comb(n, r): return nCr(n, r, fact, inv)

def perm(n, r): return nPr(n, r, fact, inv)

def homo(n, r): return nHr(n, r, fact, inv)

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    A.reverse()
    X=[]
    for i in range(M):
        X.append(int(input()))
    X.sort()
    X.reverse()
    X.append(0)
    X.append(0)
    cnt=0
    i=0
    j=0
    while i<N and j<M:
        if X[j]<A[i]:
            j+=1
        else:
            i+=1
            j+=1
            cnt+=1
    print(cnt)




















































































































































































































































































































































































































































































































































if __name__ == '__main__':
    main()
