
import itertools
# My answer

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Making permutations of size N
permutations = []
for i in range(N):
    permutations.append(i+1)

permutations = list(itertools.permutations(permutations))

print(abs(permutations.index(P)-permutations.index(Q)))
