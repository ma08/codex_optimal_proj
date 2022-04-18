

import sys
import collections

def main():
    n, m = map(int, sys.stdin.readline().split())
    x = map(int, sys.stdin.readline().split())
    for i in range(m):
        y = map(int, sys.stdin.readline().split())
        print(x[y[0]], end=" ")
        x[y[0]] = y[1]
    print()

if __name__ == "__main__":
    main()
