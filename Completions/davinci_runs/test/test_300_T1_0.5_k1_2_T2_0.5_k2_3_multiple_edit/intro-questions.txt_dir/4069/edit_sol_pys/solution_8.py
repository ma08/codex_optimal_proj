

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if N == 1:
        print(a[0])
        exit()
    if a[0] != a[1]:
        print(a[0])
        exit()
    if a[-1] != a[-2]:
        print(a[-1])
        exit()
    for i in range(1, N - 1):
        if a[i - 1] != a[i] and a[i] != a[i + 1]:
            print(a[i])
            exit()
    else:
        print(a[0])

if __name__ == '__main__':
    main()
