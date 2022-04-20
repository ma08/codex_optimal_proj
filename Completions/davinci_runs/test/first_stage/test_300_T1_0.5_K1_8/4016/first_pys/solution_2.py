

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    t = sys.stdin.readline().strip()
    if k == 1:
        print(t)
    else:
        print(t * (k - 1) + t[:n - (k - 2)])

if __name__ == "__main__":
    main()