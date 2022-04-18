
# Read inputs
A, B = map(int, input().split())

# Compute
K = (A + B) // 2

# Check if K satisfies the condition
if abs(A - K) == abs(B - K):
    print(K)
else:
    print("IMPOSSIBLE")
