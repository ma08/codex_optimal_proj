

# Read input from STDIN. Print output to STDOUT
a, b, k = map(int, input().split())

# Compute
if a >= k:
    a -= k
else:
    k -= a
    a = 0
    if b >= k:
        b -= k
    else:
        b = 0

# Print output to STDOUT
print(a, b)
