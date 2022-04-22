

# My answer
# Making permutations of size N
def permutation(n, r):
    if r == 0:
        return
    for i in range(n-1, -1, -1):
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]
        permutation(n-1, r-1)
        permutations[i], permutations[n-1] = permutations[n-1], permutations[i]


# Counting the order of P and Q
def order_check(l, p, q):
    p_order = 0
    q_order = 0
    for i in range(len(l)):
        if l[i] == p:
            p_order = i+1
        if l[i] == q:
            q_order = i+1
    return abs(p_order-q_order)



N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

permutations = []
for i in range(N):
    permutations.append(i+1)

permutation(N, N)

print(order_check(permutations, P, Q))
