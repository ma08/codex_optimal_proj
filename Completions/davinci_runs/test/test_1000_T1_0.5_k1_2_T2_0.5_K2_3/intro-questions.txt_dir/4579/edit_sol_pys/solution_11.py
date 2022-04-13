

import sys

# Read input from stdin.
N = int(sys.stdin.readline())
items = [int(x) for x in sys.stdin.readline().split()]
M = int(sys.stdin.readline())
queries = [int(x) for x in sys.stdin.readline().split()]

# Output result
for query in queries:
    print(sum(1 for item in items if item == query))
