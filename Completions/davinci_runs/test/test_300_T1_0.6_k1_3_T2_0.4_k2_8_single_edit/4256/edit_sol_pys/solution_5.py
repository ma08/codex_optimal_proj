

import sys


def main():
    # input()
    a, b, c = map(int, input().rstrip().split())

    # main()
    ans = min(b // a, c)

    # output()
    print(ans, end="")


if __name__ == '__main__':
    main()
