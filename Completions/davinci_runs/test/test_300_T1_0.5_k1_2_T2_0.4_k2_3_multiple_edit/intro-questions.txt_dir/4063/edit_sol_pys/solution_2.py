

# imports
import sys
import math

# functions
def input():
    return sys.stdin.readline().strip()

# main
N = int(input())
d = list(map(int, input().split()))

# sorting
d.sort()

# number of problems solved
count = 0

# solve
for i in range(N//2):
    if d[i] == d[N//2]:
        count += 1
    elif d[i] < d[N//2]:
        break

print(count)
