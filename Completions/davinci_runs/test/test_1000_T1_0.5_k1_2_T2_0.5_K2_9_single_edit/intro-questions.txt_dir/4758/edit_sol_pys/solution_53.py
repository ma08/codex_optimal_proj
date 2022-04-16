# https://codeforces.com/contest/1343/problem/A

from itertools import product

N, T, M = map(int, input().split())
print(len(set(product(range(N), range(T), range(M)))))
