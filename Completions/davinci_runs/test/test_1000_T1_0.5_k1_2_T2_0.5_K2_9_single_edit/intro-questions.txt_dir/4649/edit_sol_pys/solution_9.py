"""
https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
"""

import sys

if __name__ == "__main__":
    q = int(sys.stdin.readline())

    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()

        if n % 3 == 0:
            print(0)
        else:
            if k == 1:
                print(1)
            elif k == 2:
                if n % 3 == 1:
                    print(2)
                else:
                    print(1)
            else:
                if n % 3 == 2:
                    print(1)
                else:
                    print(2)
