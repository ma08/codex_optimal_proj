

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
    if len(r) == 1 and len(c) == 1:
        print('YES')
        print('0'*m)
        print('0'*n)
    elif len(c) == 1:
        print('YES')
        print('0'*m)
        print('1'*n)
    else:
        print('NO')

if __name__ == '__main__':
    main()
