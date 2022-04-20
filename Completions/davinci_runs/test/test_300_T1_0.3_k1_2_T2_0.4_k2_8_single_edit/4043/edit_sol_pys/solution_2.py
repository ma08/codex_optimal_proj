
import sys

if __name__ == '__main__':
    n, d, k = map(int, input().split())
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i, i+1)
        else:
            print('NO')
    elif d == 2:

    if d == 1:
        print('YES')
        for i in range(1, n):
            print(i, i+1)
    elif d == 3:
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i, i+1)
        else:
            if n == 3:
                print('NO')
            else:
                print('YES')
                print(1, 2)
                print(1, 3)
                print(1, 4)
                print(2, 5)
                print(2, 6)
                print(3, 7)
                print(3, 8)
                print(4, 9)
                print(4, 10)
    elif d == 4:
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i, i+1)
        else:
            if n == 4:
                print('NO')
            else:
                print('YES')
                print(1, 2)
                print(1, 3)
                print(1, 4)
                print(2, 5)
                print(2, 6)
                print(3, 7)
                print(3, 8)
                print(4, 9)
                print(4, 10)
                print(5, 11)
                print(6, 12)
                print(7, 13)
                print(8, 14)
                print(9, 15)
                print(10, 16)
    elif d == 5:
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i, i+1)
        else:
            if n == 5:
                print('NO')
            else:
                print('YES')
                print(1, 2)
                print(1, 3)
                print(1, 4)
                print(2, 5)
                print(2, 6)
                print(3, 7)
                print(3, 8)
                print(4, 9)
                print(4, 10)
                print(5, 11)
                print(6, 12)
                print(7, 13)
                print(8, 14)
                print(9, 15)
                print(10, 16)
                print(11, 17)
                print(12, 18)
                print(13, 19)
                print(14, 20)
                print(15, 21)
                print(16, 22)
    else:
        print('NO')
