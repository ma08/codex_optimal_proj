

import sys


def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        lengths = list(map(int, sys.stdin.readline().split()))
        if max(lengths) < sum(lengths) - max(lengths):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
