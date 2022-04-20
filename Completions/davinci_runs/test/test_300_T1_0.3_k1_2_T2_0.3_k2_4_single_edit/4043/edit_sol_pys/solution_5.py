

import sys

def main():
    n, d, k = map(int, sys.stdin.readline().split())
    if n <= d * k:
        print('YES')
        for i in range(1, n):
            print(i, i + 1)
        return
    else:
        print('NO')
        return

if __name__ == '__main__':
    main()
