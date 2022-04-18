
import sys

n = int(sys.stdin.readline())


def solve(x):
    while x % 10 == 0:
        x //= 10
    return x + 1 if x != 0 else 1
    
print(solve(n))
