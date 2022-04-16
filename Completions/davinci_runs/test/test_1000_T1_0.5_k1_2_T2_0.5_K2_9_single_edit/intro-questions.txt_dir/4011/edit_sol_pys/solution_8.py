

import sys

def main():
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip()))
    f = list(map(int, sys.stdin.readline().strip().split()[:m]))
    for i in range(len(num)):
        num[i] = f[num[i]-1]
    print(''.join(map(str, num)))


if __name__ == '__main__':
    main()
