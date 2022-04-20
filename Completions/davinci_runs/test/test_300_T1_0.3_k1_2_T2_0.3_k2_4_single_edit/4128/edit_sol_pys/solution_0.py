
import sys

def solve(n, m):
    return n//2 + m//2

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(solve(n, m))
