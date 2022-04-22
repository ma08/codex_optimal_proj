

# My answer 

N = 3
P = [1, 2, 3]
Q = [1, 3, 2]

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
    if permutations[i] == P[0]:
        if permutations[i+1] == P[1]:
            if permutations[i+2] == P[2]:
                P_order = i+1
    if permutations[i] == Q[0]:
        if permutations[i+1] == Q[1]:
            if permutations[i+2] == Q[2]:
                Q_order = i+1

print(abs(P_order-Q_order))
