import sys

# Read input from stdin
N = int(input())
items = [input() for _ in range(N)]

# Solve
result = len(set(items))

# Output result
print(result)
