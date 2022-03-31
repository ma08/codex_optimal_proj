
import sys

def solve(n, x):
    x.sort()
    return min(x[n//2]-x[0], x[n-1]-x[n//2])

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    x = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(n, x))
