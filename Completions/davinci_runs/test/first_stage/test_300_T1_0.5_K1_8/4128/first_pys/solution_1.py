

import sys

def solve(n):
    return (n-1)//2

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        print(solve(n))