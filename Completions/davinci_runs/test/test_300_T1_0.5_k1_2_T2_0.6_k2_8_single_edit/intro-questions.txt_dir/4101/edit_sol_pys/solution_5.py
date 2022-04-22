

def main():
    n, m = map(int, input().split())
    a = [[int(x) for x in input().split()] for _ in range(n)]
    r, c = -1, -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r.append(i)
                c.append(j)
                break
    if r == -1:
        print('YES')
        print('0'*n)
        print('0'*m)
    elif c == -1:
        print('YES')
        print('1'*n)
        print('0'*m)
    else:
        print('NO')

if __name__ == '__main__':
    main()
