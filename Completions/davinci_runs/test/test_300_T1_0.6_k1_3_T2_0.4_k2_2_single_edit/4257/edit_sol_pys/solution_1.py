
import sys


def main():
    a = int(sys.stdin.readline())
    b, c = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline()
    print("{} {}".format(a + b + c, s))


if __name__ == '__main__':
    main()
