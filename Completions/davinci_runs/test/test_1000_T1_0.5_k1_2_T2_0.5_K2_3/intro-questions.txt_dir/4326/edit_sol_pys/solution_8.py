
import sys

# N = int(input())
N = int(sys.stdin.readline())

def solve(n):
    if n < 3:
        return 0
    elif n % 3 == 0:
        return n // 3 + 1 # for 2
    else:
        return n // 3 # for 1

print(solve(N))
