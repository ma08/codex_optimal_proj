

# My answer

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Making permutations of size N
permutations = []
for i in range(N):
    permutations.append(i+1)

def permutation(n, r):
    if r == 0:
        return
    for i in range(n-1, -1, -1):
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]
        permutation(n-1, r-1)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]

permutation(N, N)

# Counting the order of P and Q
P_order = 0
Q_order = 0
for i in range(len(permutations)-1):
    if permutations[i] == P:
        P_order = i+1 # 0-index
    if permutations[i] == Q:
        Q_order = i+1 # 0-index

print(abs(P_order-Q_order))
