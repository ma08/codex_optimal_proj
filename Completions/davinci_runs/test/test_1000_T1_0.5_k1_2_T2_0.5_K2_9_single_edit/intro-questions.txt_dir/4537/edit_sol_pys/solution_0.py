

# Read input
a, b = map(int, input().split()) # a, b = int(input()), int(input())

# Compute the three values and print the maximum
print(max(a+b, a-b, a*b))
