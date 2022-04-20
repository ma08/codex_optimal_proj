import math


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] - a[0] > k:
        print('NO')
    else:
        print('YES')
        for i in range(n):
            print(a[i], end=' ')
            for j in range(1, math.ceil((n - i - 1) / 2)):
                print(a[i] + k, end=' ')
            for j in range(math.ceil((n - i - 1) / 2), n - i - 1):
                print(a[i], end=' ')
            print()


if __name__ == '__main__':
    main()
