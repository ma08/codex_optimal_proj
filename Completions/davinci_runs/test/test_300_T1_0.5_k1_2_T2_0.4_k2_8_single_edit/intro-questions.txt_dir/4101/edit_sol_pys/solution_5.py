

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    r, c = [0]*n, [0]*m
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r[i] = 1
                c[j] = 1
                break
    if r.count(0) == n:
        print('YES')
        print('0'*n)
        print('0'*m)
    elif c.count(0) == m:
        print('YES')
        print('1'*n)
        print('0'*m)
    else:
        print('NO')

if __name__ == '__main__':
    main()
