import math

import sys

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == m:
        print(2)
    else:
        print(1)

if __name__ == "__main__":
    main()
