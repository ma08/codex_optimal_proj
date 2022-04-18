
# Read input
A, B = map(int, input().split())

# Compute the median
K = (A + B) // 2

# Check if K satisfies the conditions
if abs(A - K) == abs(B - K):
    print(K)
else:
    print("IMPOSSIBLE")
