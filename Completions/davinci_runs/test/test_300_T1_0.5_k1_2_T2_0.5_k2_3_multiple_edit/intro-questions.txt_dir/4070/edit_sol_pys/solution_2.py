
import sys


def main():
    n = int(sys.stdin.readline())
    print(solve(n))


def solve(n):
    return (n + 1) // 2


if __name__ == '__main__':
    main()
