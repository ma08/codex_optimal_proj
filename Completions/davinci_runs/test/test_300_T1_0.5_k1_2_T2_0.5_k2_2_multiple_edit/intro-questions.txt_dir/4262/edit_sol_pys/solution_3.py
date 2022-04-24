

# My answer

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Making permutation of size N
permutations = list(range(1, N+1))

def permutation(n):
    if n == 1:
        return permutations
    permutation(n-1)
    for i in range(n-1):
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]
    return permutations

permutation(N, N)

# Counting the order of P and Q in permutation
P_order = 0
Q_order = 0
for i in range(len(permutations)):
    if permutations[i] == P:
        P_order = i+1
    if permutations[i] == Q:
        Q_order = i+1

print(abs(P_order-Q_order))
