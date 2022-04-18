

import sys

def main():
    x, y = map(int, sys.stdin.readline().split())  # noqa
    if x == 0:
        print("ALL GOOD" if y == 1 else "IMPOSSIBLE")
    else:
        print(x / (y - 1))  # noqa

if __name__ == "__main__":
    main()
