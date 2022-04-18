
def main():
    n, m = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    t = [0] * n
    for j in range(m):
        for i in range(n):
            t[i] = max(t[i], max(t)) + p[i][j]
    print(*t)

if __name__ == '__main__':
    main()
