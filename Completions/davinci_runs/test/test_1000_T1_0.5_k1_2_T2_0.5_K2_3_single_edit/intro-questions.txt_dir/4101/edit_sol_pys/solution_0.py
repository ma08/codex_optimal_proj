

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-1):
        if a[i][0] == 0:
            a[i] = [0] * m
            for j in range(i+1, n):
                if a[j][0] == 0:
                    a[j] = [0] * m
                break
    if a[n-1][0] == 0:
        print('YES')
        print('0'*n)
        print('0'*m)
    elif len(c) == m:
        print('YES')
        print('1'*n)
        print('0'*m)
    else:
        print('NO')

if __name__ == '__main__':
    main()
