

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    r, c = 0, 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r = i
                c = j
                break
    if r == 0 and c == 0:
        print('NO')
    elif r == 0:
        print('YES')
        print('0'*n)
        print('0'*m)
    elif c == 0:
        print('YES')
        print('1'*n)
        print('0'*m)
    else:
        print('NO')

if __name__ == '__main__':
    main()
