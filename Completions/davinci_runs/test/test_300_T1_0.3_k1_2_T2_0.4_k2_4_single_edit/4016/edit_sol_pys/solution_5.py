

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    t = sys.stdin.readline().strip()
    print(t * (k // n) + t[:k % n], end="")

if __name__ == "__main__":
    main()
