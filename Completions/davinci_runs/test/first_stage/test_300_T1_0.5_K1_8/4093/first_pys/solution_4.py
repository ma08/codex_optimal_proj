

import sys
import math

def main():
    t = int(input())
    for i in range(t):
        n, m = [int(x) for x in input().split()]
        if n == 1:
            print(0)
        elif n == 2:
            print(m)
        elif m == 1:
            print(n - 1)
        else:
            print(max(m - 1, (m - 1) * (n - 2) + 1))

if __name__ == '__main__':
    main()