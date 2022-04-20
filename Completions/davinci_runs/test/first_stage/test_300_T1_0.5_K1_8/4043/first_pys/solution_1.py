

import sys
import numpy as np

def main():
    n, d, k = map(int, sys.stdin.readline().split())
    if d == 1:
        print("YES")
        for i in range(1, n):
            print(1, i + 1)
    elif d == 2:
        if n == 2:
            print("YES")
            print(1, 2)
        else:
            print("NO")
    elif d == 3:
        if n <= k + 1:
            print("YES")
            for i in range(1, n):
                print(1, i + 1)
        else:
            print("NO")
    elif d == 4:
        if n <= 2 * k + 1:
            print("YES")
            for i in range(1, n):
                print(1, i + 1)
        else:
            print("NO")
    else:
        print("NO")

if __name__ == '__main__':
    main()