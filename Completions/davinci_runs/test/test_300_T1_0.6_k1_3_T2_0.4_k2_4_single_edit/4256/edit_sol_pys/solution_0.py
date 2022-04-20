
import sys


def main():
    # input
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    # main
    ans = min(b // a, c)

    # output
    print(ans)


if __name__ == '__main__':
    main()
