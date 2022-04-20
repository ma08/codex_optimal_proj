

def main():
    n, m = map(int, input().split())
    A = list()
    for i in range(n):
        A.append(list(map(int, input().split())))
    
    ans = 0
    for j in range(m):
        for i in range(n):
            if A[i][j] != (i * m) + j + 1:
                ans += 1
                for k in range(i+1, n):
                    if A[k][j] == (i * m) + j + 1:
                        A[i][j], A[k][j] = A[k][j], A[i][j]
                        break
    print(ans)

if __name__ == '__main__':
    main()