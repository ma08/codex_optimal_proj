

# My answer

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

# Making permutations of size n
permutations = []
for i in range(n):
    permutations.append(i+1)

def permutation(n, r):
    if r == 0:
        return
    for i in range(n-1, -1, -1):
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]
        permutation(n-1, r-1)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]

permutation(n, n)

# Counting the order of P and Q
p_order = 0
q_order = 0
for i in range(len(permutations)):
    if permutations[i] == p:
        p_order = i+1
    if permutations[i] == q:
        q_order = i+1

print(abs(p_order-q_order))
