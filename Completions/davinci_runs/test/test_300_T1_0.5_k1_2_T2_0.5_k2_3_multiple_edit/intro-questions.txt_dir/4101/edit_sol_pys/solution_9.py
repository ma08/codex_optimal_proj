

def main():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    R, C = [], []
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                R.append(i)
                C.append(j)
    if len(R) == n or len(C) == m:
        print('YES') 
        if len(R) == n:
            print('0'*n)
            print('0'*m)
        else:
            print('1'*n)
            print('0'*m)
    else:
        print('NO')

if __name__ == '__main__':
    main()
