

import sys


def main():
    d, n = list(map(int, input().split()))
    if d == 0:
        print(n)
    elif d == 1:
        print(n * 100 + 5)
    else:
        print(n * 100 + 50)

if __name__ == "__main__":
    main()
