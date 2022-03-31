
import sys

def f(x):
    while x % 10 == 0: x //= 10
    return x + 1

def solve(n):
    seen = set([n])
    for i in range(n+1):
        seen.add(f(i))
    return len(seen)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))
