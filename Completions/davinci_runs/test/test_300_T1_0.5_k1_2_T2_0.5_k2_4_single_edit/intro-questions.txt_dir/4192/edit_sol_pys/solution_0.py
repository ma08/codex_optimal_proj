

import sys


def main():
    line = sys.stdin.readline()
    d, t, s = map(int, line.split())
    if d / s <= t:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
