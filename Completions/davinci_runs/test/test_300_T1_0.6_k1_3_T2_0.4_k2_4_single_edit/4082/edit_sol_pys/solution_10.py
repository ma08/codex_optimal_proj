
def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                a[i][j] = 0
            else:
                a[i][j] = 1
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                a[i][j] = 0
                for k in range(n):
                    if a[k][j] == 1:
                        a[k][j] = 0
                for l in range(m):
                    if a[i][l] == 1:
                        a[i][l] = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                print('NO')
                return
    print('YES')

if __name__ == '__main__':
    main()
