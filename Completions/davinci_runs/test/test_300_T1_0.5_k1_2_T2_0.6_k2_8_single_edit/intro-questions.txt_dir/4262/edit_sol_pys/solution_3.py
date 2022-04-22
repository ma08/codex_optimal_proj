
# My answer

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Making permutations of size N
permutations = []
for i in range(1, N+1):
    permutations.append(i)

def permutation(n, r):
    if r == 0:
        return
    for i in range(n-1, 0, -1):
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]
        permutation(n-1, r-1)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]

permutation(N, N)

# Counting the index of P and Q
P_index = 0
Q_index = 0
for i in range(len(permutations)):
    if permutations[i] == P[0]:
        P_index = i+1
    if permutations[i] == Q[0]:
        Q_index = i+1

print(abs(P_order-Q_order))
