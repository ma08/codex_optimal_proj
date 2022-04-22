

import sys


def main():
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    for i in a:
        print(i, end=' ')



if __name__ == '__main__':
    main()
