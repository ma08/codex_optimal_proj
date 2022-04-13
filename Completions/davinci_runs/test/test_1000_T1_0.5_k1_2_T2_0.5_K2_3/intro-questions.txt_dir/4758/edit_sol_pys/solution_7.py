from itertools import product

N, T, M = map(int, input().split())

print(len(set(product(range(1, N+1), range(1, T+1), range(1, M+1)))))
