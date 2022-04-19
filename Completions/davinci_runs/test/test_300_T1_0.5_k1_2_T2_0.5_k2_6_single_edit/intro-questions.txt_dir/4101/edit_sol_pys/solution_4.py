

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    r, c = [], []
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r.append(i)
                c.append(j)
                break
    if len(r) == n:
        print('YES')
        print('0'*n, sep='\n')
        print('0'*m, sep='\n')
    elif len(c) == m:
        print('YES')
        print('1'*n, sep='\n')
        print('0'*m, sep='\n')
    else:
        print('NO')

if __name__ == '__main__':
    main()
