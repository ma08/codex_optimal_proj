

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    c = 0
    for i in range(n-1):
        if a[i] == 0:
            c += 1
            a[i] = 1
        if a[i] > 0 and a[i+1] < 0:
            c += 1
            a[i+1] = 1
        if a[i] < 0 and a[i+1] > 0:
            c += 1
            a[i+1] = -1

    print(c)

if __name__ == '__main__':
    main()