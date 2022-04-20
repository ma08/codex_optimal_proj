

import sys

def main():
    n, d, k = map(int, sys.stdin.readline().split())
    if d == 1 and n <= k:
        print('YES')
        for i in range(1, n):
            print(i, i + 1)
        return
    if d == 2 and n <= 2 * k:
        print('YES')
        for i in range(1, n):
            print(i, i + 1)
        return
    if d == 3 and n <= 3 * k:
        print('YES')
        for i in range(1, n):
            print(i, i + 1)
        return
    if d == 4 and n <= 4 * k:
        print('YES')
        for i in range(1, n):
            print(i, i + 1)
        return
    if d == 5 and n <= 5 * k:
        print('YES')
        for i in range(1, n):
            print(i, i + 1)
        return
    print('NO')

if __name__ == '__main__':
    main()
