
# Read input
a, b, c = map(int, input().split())

# Calculate amount of water in bottle2
bottle2 = c - (a - b)

# Print result
print(max(0, bottle2))
