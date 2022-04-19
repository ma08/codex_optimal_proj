# -*- coding: utf-8 -*-

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    for i in range(m):
        if all([a[j][i] == 0 for j in range(n)]):
            print('YES')
            print('0'*n)
            print('0'*m)
            exit()
    print('NO')

if __name__ == '__main__':
    main()
