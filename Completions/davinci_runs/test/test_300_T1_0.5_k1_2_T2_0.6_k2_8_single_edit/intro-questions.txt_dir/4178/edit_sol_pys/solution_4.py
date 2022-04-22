


def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = 1 if a[i][j] == b[i][j] else 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                for k in range(m):
                    a[i][k] = 1 - a[i][k]
                for k in range(n):
                    a[k][j] = 1 - a[k][j]
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                print('NO')
                return
    print('YES')



if __name__ == '__main__':
    solve()
