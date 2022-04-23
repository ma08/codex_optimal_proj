

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    r, c = [], [0]*m
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r.append(i)
                c[j] += 1
                break
    if len(r) == n:
        print('YES')
        print('0'*m)
        print('0'*n)
    elif len(c) == m:
        print('YES')
        print('1'*m)
        print('0'*n)
    else:
        print('NO')

if __name__ == '__main__':
    main()
