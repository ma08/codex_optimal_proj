
# Read input.
A, B = map(int, input().split())

# Compute the middle.
K = (A + B) // 2

# Check if K satisfies the condition. If so, print K.
if abs(A - K) == abs(B - K):  # abs(a - b) is the absolute value of a - b.
    print(K)
else:
    print("IMPOSSIBLE")
