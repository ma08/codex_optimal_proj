
import sys


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        print(a[i])


if __name__ == '__main__':
    main()
