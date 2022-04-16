
from itertools import combinations

N, T, M = map(int, input().split())
print(len(set(combinations(range(N), range(T), range(M)))))
