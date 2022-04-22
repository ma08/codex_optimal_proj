
# Import
import sys, math

# Functions
def input(): return sys.stdin.readline().strip()

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Main
N = int(input()) # Number of problems
d = list(map(int, input().split())) # Difficulty

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
