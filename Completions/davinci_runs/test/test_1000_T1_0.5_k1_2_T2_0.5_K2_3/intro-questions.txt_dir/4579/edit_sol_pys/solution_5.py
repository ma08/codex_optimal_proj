import sys

# Get input
N = int(input())
items = [input() for _ in range(N)]

# Solve the problem
result = len(set(items))

# Print result
print(result)
