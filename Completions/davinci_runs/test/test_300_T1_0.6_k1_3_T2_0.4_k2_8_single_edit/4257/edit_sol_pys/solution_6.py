
import sys


def main():
    a, b = map(int, sys.stdin.readline().split())  # read two integers
    print(a * b)  # print their product


if __name__ == '__main__':
    main()
