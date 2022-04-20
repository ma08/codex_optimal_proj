

# Read input and split
a, b, k = input().split()

# Convert to int
a = int(a)
b = int(b)
k = int(k)

# Compute and print output
print(a - k if a >= k else 0, b - (k - a) if a < k else b)

# Print output
