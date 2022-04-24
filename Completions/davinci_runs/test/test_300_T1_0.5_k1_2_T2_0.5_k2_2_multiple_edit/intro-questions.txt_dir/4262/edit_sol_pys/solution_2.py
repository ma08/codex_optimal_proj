

# My answer

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Making permutation of size N
permutations = [0]*N
for i in range(N):
    permutations[i] = i+1

def permutation(n, r):
    if r == 0:
        return
    for i in range(n-1, -1, -1):  # range(start, stop, step)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]
        permutation(n-1, r-1)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]

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
