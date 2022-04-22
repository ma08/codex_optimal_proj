

import sys

def main():
    n = int(sys.stdin.readline())
    num = sys.stdin.readline().strip()
    f = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(len(num) - 1):
        print(f[int(num[i]) - 1], end='')
    print(f[int(num[-1]) - 1])


if __name__ == '__main__':
    main()
