

import sys


def main():
    n, k = map(int, sys.stdin.readline().split())  # n = number of letters in the string, k = number of letters to print
    t = sys.stdin.readline().strip()
    print(t * (k // n) + t[:k % n])

if __name__ == "__main__":
    main()
