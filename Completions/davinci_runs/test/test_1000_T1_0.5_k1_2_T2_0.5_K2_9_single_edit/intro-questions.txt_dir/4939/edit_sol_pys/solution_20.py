import math

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a = sorted(a)
    print(a)
    ans = 0
    for i in range(1, n):
        ans += a[i] - a[i - 1]
    print(ans)


main()
