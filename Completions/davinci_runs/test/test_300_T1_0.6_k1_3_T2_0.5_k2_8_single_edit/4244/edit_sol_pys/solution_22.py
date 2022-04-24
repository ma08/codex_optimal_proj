
import sys

# Calculate mean of all x coordinates
# Store differences between mean and all x coordinates in a list
# Return the sum of all differences

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

mean = sum(x) / n

diff = [abs(mean - x[i]) for i in range(n)]

print(int(sum(diff)))
