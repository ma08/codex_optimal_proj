import sys


def main():
    a, b = map(int, sys.stdin.readline().split())  # get two integers
    print(a * b)  # print the product of the two integers


if __name__ == '__main__':
    main()
