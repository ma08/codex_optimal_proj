

import sys

def main():
    n = int(sys.stdin.readline())
    num = map(int, sys.stdin.readline().strip().split())
    f = map(int, sys.stdin.readline().strip().split())
    for i in range(len(num)):
        num[i] = f[num[i] - 1]
    print(''.join(map(str, num)))


if __name__ == '__main__':
    main()
