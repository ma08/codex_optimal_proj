

def main():
    n, m = map(int, input().split())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    B = []
    for _ in range(m):
        B.append(int(input()))
    for i in range(n):
        ans = 0
        for j in range(m):
            ans += A[i][j] * B[j]
        print(ans)
    return

if __name__ == '__main__':
    main()
