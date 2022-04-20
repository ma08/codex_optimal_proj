
import sys

# Read input
n, k = map(int, sys.stdin.readline().split())

# Find all positive integers that divide n
divisors = [i for i in range(1, n + 1) if n % i == 0]

# Print the k-th smallest positive integer that divides n
print(divisors[-k])
