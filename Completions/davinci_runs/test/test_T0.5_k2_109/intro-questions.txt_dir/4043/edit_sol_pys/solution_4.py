
import sys

def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, d, k = next(reader)
    if d == 1:
        print('YES')
        for i in range(n - 1):
            print(i + 1, i + 2)
    elif d == 2:
        if k >= n - 1:
            print('YES')
            for i in range(n - 1):
                print(i + 1, i + 2)
        else:
            print('NO')
    elif d == 3:
        if k >= n // 2:
            print('YES')
            for i in range(n // 2):
                print(i + 1, i + 2)
            for i in range(n // 2 - 1):
                print(i + 1, n // 2 + i + 1)
            print(n // 2, n)
        else:
            print('NO')
    elif d == 4:
        if k >= n // 3 and n % 3 == 0:
            print('YES')
            for i in range(n // 3):
                print(i + 1, i + 2)
            for i in range(n // 3 - 1):
                print(i + 1, n // 3 + i + 1)
            for i in range(n // 3 - 1):
                print(i + 1, 2 * n // 3 + i + 1)
            print(2 * n // 3, n - 1)
            print(n - 1, n - 2)
        else:
            print('NO')
    elif d == 5:
        if k >= n // 4 and n % 4 == 0:
            print('YES')
            for i in range(n // 4):
                print(i + 1, i + 2)
            for i in range(n // 4 - 1):
                print(i + 1, n // 4 + i + 1)
            for i in range(n // 4 - 1):
                print(i + 1, 2 * n // 4 + i + 1)
            for i in range(n // 4 - 1):
                print(i + 1, 3 * n // 4 + i + 1)
            print(3 * n // 4, n - 3)
            print(n - 3, n - 2)
            print(n - 2, n - 1)
        else:
            print('NO')
    elif d == 6:
        if k >= n // 5 and n % 5 == 0:
            print('YES')
            for i in range(n // 5):
                print(i + 1, i + 2)
            for i in range(n // 5 - 1):
                print(i + 1, n // 5 + i + 1)
            for i in range(n // 5 - 1):
                print(i + 1, 2 * n // 5 + i + 1)
            for i in range(n // 5 - 1):
                print(i + 1, 3 * n // 5 + i + 1)
            for i in range(n // 5 - 1):
                print(i + 1, 4 * n // 5 + i + 1)
            print(n - 4, n - 3)
            print(n - 3, n - 2)
            print(n - 2, n - 1)
            print(n - 1, n)
        else:
            print('NO')
    elif d == 7:
        if k >= n // 6 and n % 6 == 0:
            print('YES')
            for i in range(n // 6):
                print(i + 1, i + 2)
            for i in range(n // 6 - 1):
                print(i + 1, n // 6 + i + 1)
            for i in range(n // 6 - 1):
                print(i + 1, 2 * n // 6 + i + 1)
            for i in range(n // 6 - 1):
                print(i + 1, 3 * n // 6 + i + 1)
            for i in range(n // 6 - 1):
                print(i + 1, 4 * n // 6 + i + 1)
            for i in range(n // 6 - 1):
                print(i + 1, 5 * n // 6 + i + 1)
            print(n - 5, n - 4)
            print(n - 4, n - 3)
            print(n - 3, n - 2)
            print(n - 2, n - 1)
            print(n - 1, n)
        else:
            print('NO')
    else:
        print('NO')


if __name__ == '__main__':
    main()
