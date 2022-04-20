


def main():
    n, k = map(int, input().split())
    if k == 1:
        print('NO')
        return
    elif n == 2:
        print('YES')
        print(1, k)
        print(k, 1)
        return
    elif n == k:
        print('YES')
        for i in range(1, k):
            print(i, i + 1)
        print(k, 1)
        return
    elif n == k + 1:
        print('YES')
        for i in range(1, k):
            print(i, i + 1)
        print(k, 2)
        print(2, 1)
        return
    else:
        print('YES')
        for i in range(1, k):
            print(i, i + 1)
        print(k, 2)
        print(2, 1)
        for i in range(k + 2, n):
            print(1, 2)
        return


if __name__ == '__main__':
    main()