from itertools import product

N, T, M = map(int, input().split())
print(len(set(product(range(N), range(T), range(M)))))
