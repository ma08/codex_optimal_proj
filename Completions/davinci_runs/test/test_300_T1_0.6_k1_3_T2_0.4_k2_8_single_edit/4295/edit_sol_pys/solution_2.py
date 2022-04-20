

from sys import stdin

# Read from standard input 
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

# Sort the list
A.sort()

# Print the last element
print(A[-1])
