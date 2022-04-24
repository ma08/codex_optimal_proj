import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(min_num_operations(n, k, a), end="")


def min_num_operations(n, k, a):
    return n - k


if __name__ == '__main__':
    main()
