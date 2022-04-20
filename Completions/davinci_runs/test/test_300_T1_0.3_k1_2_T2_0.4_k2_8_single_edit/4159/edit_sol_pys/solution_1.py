
# Read input
a, b, k = map(int, input().split()) # a, b, k = (int(i) for i in input().split())

# Compute
if a >= k: a -= k
else: k -= a; a = 0; b = max(b - k, 0)

# Print output
print(a, b)
