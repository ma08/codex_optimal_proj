

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    c = [list(map(int, input().split())) for _ in range(n)]
    d = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            print(a[i][j] + b[i][j] + c[i][j] + d[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()
