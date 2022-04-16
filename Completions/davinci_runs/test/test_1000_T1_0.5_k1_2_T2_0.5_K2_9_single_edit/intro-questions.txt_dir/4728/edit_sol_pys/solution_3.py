

def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                print('YES')
                print(1, a[i])
                return
    print('NO')


main()
