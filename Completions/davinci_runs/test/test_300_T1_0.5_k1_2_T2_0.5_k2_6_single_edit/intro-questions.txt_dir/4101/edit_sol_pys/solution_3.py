

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    r, c, flag = [], [], 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r.append(i)
                c.append(j)
                flag = 1
    if flag == 0:
        print('NO')
    elif len(r) == n:
        print('YES')
        print('0'*(n-1)+'1')
        print('0'*m+'1')
    elif len(c) == m:
        print('YES')
        print('1'*(n-1)+'0')
        print('0'*m)
    else:
        print('NO')

if __name__ == '__main__':
    main()
