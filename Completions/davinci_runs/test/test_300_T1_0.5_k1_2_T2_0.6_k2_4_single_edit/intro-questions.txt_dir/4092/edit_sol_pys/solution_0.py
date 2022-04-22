

import sys, os

def main():
    n, m = sys.stdin.readline().split()
    n, m = int(n), int(m)
    l = []
    for i in range(n):
        l.append(sys.stdin.readline())
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(l[i - 1], end = '')
        else:
            print(l[i - 1][::-1], end = '')


if __name__ == '__main__':
    main()
