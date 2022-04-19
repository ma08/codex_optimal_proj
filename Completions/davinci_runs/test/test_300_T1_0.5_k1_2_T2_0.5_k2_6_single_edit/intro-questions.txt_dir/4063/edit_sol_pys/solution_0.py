

# Import
import sys
import math

# Functions
def input():
    return sys.stdin.readline().strip()

# Main
N = int(input())
d = list(map(int, input().split()))

# Sorting
d.sort()

# Number of problems
count = 0

# Solve
for i in range(N//2):
    if d[i] == d[N//2]:
        count += 1
    elif d[i] != d[N//2]:
        break

print(count)
