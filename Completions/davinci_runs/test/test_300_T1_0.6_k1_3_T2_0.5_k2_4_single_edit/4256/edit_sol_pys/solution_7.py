

import sys


def main():
    # input
    a, b = map(int, sys.stdin.readline().rstrip().split())

    # main
    ans = b // a

    # output
    print(ans)


if __name__ == '__main__':
    main()
