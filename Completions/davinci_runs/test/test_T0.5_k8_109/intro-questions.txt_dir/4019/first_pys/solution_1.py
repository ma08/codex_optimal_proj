


def main():
    n, m, d = map(int, input().split())
    if d == n - 1:
        print('YES')
        for i in range(2, n + 1):
            print(1, i)
    elif d == 1:
        print('YES')
        for i in range(1, n):
            print(i, i + 1)
    elif m == n - 1:
        print('NO')
    else:
        print('YES')
        for i in range(2, n):
            print(1, i)
        print(1, n)


if __name__ == '__main__':
    main()