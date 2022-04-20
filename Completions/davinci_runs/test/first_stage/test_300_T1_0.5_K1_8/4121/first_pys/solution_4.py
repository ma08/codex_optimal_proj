

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = [*map(int, sys.stdin.readline().strip().split())]
    a.sort()
    print(a)
    if a[0] == a[-1]:
        print('YES')
        return
    if a[0] + 1 == a[1] and a[-2] + 1 == a[-1]:
        print('YES')
        return
    print('NO')


if __name__ == '__main__':
    main()