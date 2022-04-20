
import sys

# Read input from stdin
n = int(sys.stdin.readline())

# Initialize the array
arr = [0] * n

# Read the array
arr = list(map(int, sys.stdin.readline().split()))

# Print the sum
print(sum(arr))
