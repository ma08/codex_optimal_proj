
# Import
import sys

# Main
N = int(sys.stdin.readline().strip())
d = list(map(int, sys.stdin.readline().strip().split()))

# Sorting
d.sort()

# Number of problems
count = 0

# Solve
for i in range(N//2):
    if d[i] == d[N//2]:
        count += 1
    elif d[i] < d[N//2]:
        break

print(count)
