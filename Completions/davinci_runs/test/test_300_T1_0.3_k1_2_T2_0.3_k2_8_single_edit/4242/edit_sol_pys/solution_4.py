
import sys

# Read input from stdin
a, b, k = map(int, sys.stdin.readline().split()) # map() applies int() to every element of the list returned by split()

# Find all positive integers that divide both a and b
divisors = []
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        divisors.append(i)

# Print the k-th largest positive integer that divides both a and b
print(divisors[-k])
