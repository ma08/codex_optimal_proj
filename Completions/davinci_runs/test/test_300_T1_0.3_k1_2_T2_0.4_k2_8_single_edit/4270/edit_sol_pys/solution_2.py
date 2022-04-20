
import math


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if a[-1] < b[0]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
