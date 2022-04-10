

import sys

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    print(min(x[i] - x[i-1] for i in range(1, n)))

if __name__ == "__main__":
    solve()