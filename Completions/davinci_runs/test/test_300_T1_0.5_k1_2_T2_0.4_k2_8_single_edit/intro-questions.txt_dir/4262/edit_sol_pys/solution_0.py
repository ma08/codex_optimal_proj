

# My answer

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Making permutations of size N and counting the order of P and Q
permutations = []
for i in range(N):
P_order = 0
Q_order = 0
    permutations.append(i+1)

def permutation(n, r):
        global P_order
        global Q_order
        if permutations == P:
            P_order = len(permutations)
        if permutations == Q:
            Q_order = len(permutations)
    if r == 0:
        return
    for i in range(n-1, -1, -1):
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]
        permutation(n-1, r-1)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]

permutation(N, N)

print(abs(P_order-Q_order))
