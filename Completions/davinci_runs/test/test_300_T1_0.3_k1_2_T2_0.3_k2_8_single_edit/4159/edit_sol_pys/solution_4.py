#!/usr/bin/env python3

# Read input
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

# Print output
print(a, b)
