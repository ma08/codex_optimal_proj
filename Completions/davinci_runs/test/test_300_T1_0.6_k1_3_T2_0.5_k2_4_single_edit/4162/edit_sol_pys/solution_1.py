

import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A))


if __name__ == '__main__':
    main()
