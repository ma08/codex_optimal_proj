

import sys


def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    if abs(a - c) <= d:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
