

import sys

def solve(L, v, l, r):
    if l == 1:
        return (L - r) // v + 1
    else:
        return (L - r) // v + (l - 1) // v

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        L, v, l, r = map(int, input().split())
        print solve(L, v, l, r)
