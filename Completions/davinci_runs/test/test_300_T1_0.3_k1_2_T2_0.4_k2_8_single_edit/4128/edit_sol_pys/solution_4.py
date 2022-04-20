

import sys

def solve(n, k):
    return n//k

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = int(input())
        print(solve(n, k))
