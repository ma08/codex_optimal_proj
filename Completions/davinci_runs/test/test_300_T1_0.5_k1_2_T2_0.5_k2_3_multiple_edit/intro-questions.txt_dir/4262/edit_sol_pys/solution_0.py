

# My answer (Not the best one)

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
    for i in range(n-1, -1, -1): # from n-1 to 0 (decreasing)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]
        permutation(n-1, r-1)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]

permutation(N, N)

# Counting the order of P and Q
P_order = 0 # Order of P
Q_order = 0 # Order of Q
for i in range(len(permutations)):
    if permutations[i] == P: # Find the order of P
        P_order = i+1
    if permutations[i] == Q: # Find the order of Q
        Q_order = i+1

print(abs(P_order-Q_order))
