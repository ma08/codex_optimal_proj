

import sys

def solve(n, x):
    x.sort()
    return min(x[n//2]-x[0], x[n-1]-x[n//2])

# def solve(n, x):
#     x.sort()
#     if n%2==0:
#         return min(x[n//2]-x[0], x[n-1]-x[n//2])
#     else:
#         return min(x[n//2]-x[0], x[n-1]-x[n//2+1])

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    x = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(n, x))