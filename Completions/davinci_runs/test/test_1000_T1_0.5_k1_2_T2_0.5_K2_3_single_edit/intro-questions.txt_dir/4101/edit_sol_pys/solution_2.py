

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
    if r == set(range(n)):
        print('YES')
        print('0'*n)
        print('0'*m)
    elif c == set(range(m)):
        print('YES')
        print('1'*n)
        print('0'*m)
    else:
        print('NO')

if __name__ == '__main__':
    main()
