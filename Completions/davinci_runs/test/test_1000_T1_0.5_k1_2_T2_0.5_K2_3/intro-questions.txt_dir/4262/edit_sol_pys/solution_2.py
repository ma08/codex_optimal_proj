
import itertools
# My answer

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Making permutations of length N and storing them in a list
permutations = list(itertools.permutations(range(1, N+1)))

# Counting the order of P and Q
P_order = 0
Q_order = 0
for i in range(len(permutations)):
    if permutations[i] == P:
        P_order = i+1
    if permutations[i] == Q:
        Q_order = i+1

print(abs(P_order-Q_order))
