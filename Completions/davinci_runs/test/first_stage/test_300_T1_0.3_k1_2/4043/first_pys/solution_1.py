

import sys

def main():
    n, d, k = map(int, sys.stdin.readline().split())
    if d == 1:
        print('YES')
        for i in range(1, n):
            print(i, i + 1)
        return
    if d == 2:
        if n <= 2 * k:
            print('YES')
            for i in range(1, n):
                print(i, i + 1)
            return
        else:
            print('NO')
            return
    if d == 3:
        if n <= 3 * k:
            print('YES')
            for i in range(1, n):
                print(i, i + 1)
            return
        else:
            print('NO')
            return
    if d == 4:
        if n <= 4 * k:
            print('YES')
            for i in range(1, n):
                print(i, i + 1)
            return
        else:
            print('NO')
            return
    if d == 5:
        if n <= 5 * k:
            print('YES')
            for i in range(1, n):
                print(i, i + 1)
            return
        else:
            print('NO')
            return

if __name__ == '__main__':
    main()