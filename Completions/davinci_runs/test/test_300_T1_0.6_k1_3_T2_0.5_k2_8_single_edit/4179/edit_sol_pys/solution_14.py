import os
import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate

import sys

def main():
    N = int(read())
    ans = 0
    for i in range(1, N + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        ans += i

    print(ans)
main()
