
import sys

def solve(L, v, l, r):
    return (L - r) // v + (l - 1) // v

if __name__ == "__main__":
    t = int(raw_input())
    for _ in range(t):
        L, v, l, r = map(int, raw_input().split())
        print solve(L, v, l, r)
