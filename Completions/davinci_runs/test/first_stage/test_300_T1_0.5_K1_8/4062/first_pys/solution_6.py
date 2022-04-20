

# Read input
a, b, c, d = [int(x) for x in input().split()]

# Compute the maximum value of x*y
max_val = max(a*c, a*d, b*c, b*d)
print(max_val)