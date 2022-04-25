
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

# Number of pairs
count = 1

# Solve
for i in range(N//2+1):
    if d[i] == d[N//2+1]:
        count += 1
    elif d[i] < d[N//2+1]:
        break

print(count)
