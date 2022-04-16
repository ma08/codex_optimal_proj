
import sys

# read input
n = int(input())
items = [input() for _ in range(n)]

# solve
result = len(set(items))

# output result
print(result)
