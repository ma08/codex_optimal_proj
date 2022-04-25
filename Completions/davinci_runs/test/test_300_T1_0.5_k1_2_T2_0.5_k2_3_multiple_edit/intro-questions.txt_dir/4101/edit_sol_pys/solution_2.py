

def main():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    R, C = [], []
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                R.append(i)
                C.append(j)
                break
    if len(R) == n:
        print('YES')
        print('0'*n, sep='\n')
        print('0'*m, sep='\n')
    elif len(C) == m:
        print('YES')
        print('1'*n, sep='\n')
        print('0'*m, sep='\n')
    else:
        print('NO')

if __name__ == '__main__':
    main()
