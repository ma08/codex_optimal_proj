

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    r = ''
    c = ''
    for i in range(n):
        if sum(a[i]) % 2 == 1:
            r += '1'
        else:
            r += '0'
    for j in range(m):
        if sum(a[i][j] for i in range(n)) % 2 == 1:
            c += '1'
        else:
            c += '0'
    if r.count('1') + c.count('1') <= n + m - 1:
        print('YES')
        print(r)
        print(c)
    else:
        print('NO')

if __name__ == '__main__':
    main()