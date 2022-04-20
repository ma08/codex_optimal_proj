

# 树的直径是最大的距离
# 树的度是每个点的连通数
# 求树的直径为d，每个点的度数不超过k的树
# 如果不存在，输出NO，如果存在，输出YES，然后输出边的信息

import sys

def main():
    n, d, k = map(int, sys.stdin.readline().strip().split())

    if n == 1:
        print('YES')
        return
    if d == 1:
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i + 1, i)
            return
        else:
            print('NO')
            return
    if d == 2:
        if k >= n - 2:
            print('YES')
            for i in range(1, n - 1):
                print(i + 1, i)
            print(n, n - 1)
            return
        else:
            print('NO')
            return
    if d == 3:
        if k >= n - 2:
            print('YES')
            for i in range(2, n - 1):
                print(i + 1, i)
            print(n, n - 1)
            print(1, n)
            return
        else:
            print('NO')
            return
    if d == 4:
        if k >= n - 3:
            print('YES')
            for i in range(3, n - 1):
                print(i + 1, i)
            print(n, n - 1)
            print(1, n)
            print(2, 1)
            return
        else:
            print('NO')
            return
    if d == 5:
        if k >= n - 3:
            print('YES')
            for i in range(4, n - 1):
                print(i + 1, i)
            print(n, n - 1)
            print(1, n)
            print(2, 1)
            print(3, 2)
            return
        else:
            print('NO')
            return
    if d >= 6:
        if k >= n - 4:
            print('YES')
            for i in range(5, n - 1):
                print(i + 1, i)
            print(n, n - 1)
            print(1, n)
            print(2, 1)
            print(3, 2)
            print(4, 3)
            return
        else:
            print('NO')
            return


if __name__ == '__main__':
    main()