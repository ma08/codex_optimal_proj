

# Read input and convert to int
a, b = map(int, input().split())

# Compute
k = (a + b) // 2

# Check if K satisfies the condition
if abs(a - k) == abs(b - k):
    print(k)
else:
    print("IMPOSSIBLE")
