

import sys


def main():
    d = int(input())
    n = int(input())
    if d == 0:
        print(n)
    elif d == 1:
        print(n * 100 + 5)
    else:
        print(n * 100 + 50)

if __name__ == "__main__":
    main()
