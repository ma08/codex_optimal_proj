
def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    s = [list(map(int, input().split())) for _ in range(m)]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                if a[i][j] == s[k][0]:
                    a[i][j] = s[k][1]
    for row in a:
        print(*row)

if __name__ == '__main__':
    main()
