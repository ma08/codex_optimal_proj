

# Import
import sys
import math

# Functions
def input():

def solve(n, d):
    # Sorting
    d.sort()

    # Number of problems
    count = 0

    # Solve
    for i in range(n//2):
        if d[i] == d[n//2]:
            count += 1
        elif d[i] < d[n//2]:
            break

    return count
    return sys.stdin.readline().strip()

# Main
N = int(input())
d = list(map(int, input().split()))

print(solve(N, d))
