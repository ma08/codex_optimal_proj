

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    r, c = set(), set()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r.add(i)
                c.add(j)
                break
    if len(r) == n and len(c) == m:
        print('YES')
        print('0'*m)
        for i in range(n-1):
            print('0'*m)
    elif len(r) == n and len(c) < m:
        print('YES')
        for i in range(n-1):
            print('1'*m)
    else:
        print('NO')

if __name__ == '__main__':
    main()
