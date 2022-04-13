import sys

N = int(sys.stdin.readline())

def solve(n):
    if n < 3:
        return 0
    else:
        return n // 3 + (n % 3 > 1)

print(solve(N))
