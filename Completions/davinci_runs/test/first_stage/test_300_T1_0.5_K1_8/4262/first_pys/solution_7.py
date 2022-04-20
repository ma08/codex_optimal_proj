

from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

permutations = list(permutations(range(1, N + 1)))

print(abs(permutations.index(P) - permutations.index(Q)))