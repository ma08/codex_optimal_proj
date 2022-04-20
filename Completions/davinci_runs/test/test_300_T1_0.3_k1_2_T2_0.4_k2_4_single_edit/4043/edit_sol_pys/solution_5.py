
import sys


def main():
    n, d, k = map(int, input().split())
    print('YES')
    for i in range(1, n):
        print(i, i + 1)


if __name__ == '__main__':
    main()
