

# Read input
a, b, k = map(int, input().split())  # Read input

# Compute
if a >= k:  # If a is greater than k
    a -= k  # subtract k from a
else:  # If a is less than k
    k -= a  # subtract a from k
    a = 0  # set a to 0
    if b >= k:  # if b is greater than k
        b -= k  # subtract k from b
    else:
        b = 0

# Print output
print(a, b)
