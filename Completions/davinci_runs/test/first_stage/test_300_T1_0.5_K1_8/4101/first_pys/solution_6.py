

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    #print(a)
    r = [0] * n
    c = [0] * m
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                r[i] += 1
                c[j] += 1
    #print(r)
    #print(c)
    for i in range(n):
        for j in range(m):
            if r[i] + c[j] == n + m - 1:
                r[i] = 1 - r[i] % 2
                c[j] = 1 - c[j] % 2
                a[i][j] = 1 - a[i][j]
    #print(r)
    #print(c)
    #print(a)
    for i in range(n):
        for j in range(m):
            if a[i][j] != 1:
                print('NO')
                return
    print('YES')
    print(''.join(map(str, r)))
    print(''.join(map(str, c)))

if __name__ == '__main__':
    main()