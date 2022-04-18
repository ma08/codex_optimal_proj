

def solve(k):

# Read input
q = int(input())
k = [int(input()) for _ in range(q)]

# Solve queries
for k_i in k:
    print(solve(k_i))
