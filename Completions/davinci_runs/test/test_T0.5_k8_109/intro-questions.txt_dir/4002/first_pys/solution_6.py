

def main():
    n, m, k = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    f = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                f[i][j] = a[i][j]
            else:
                f[i][j] = a[i][j] + max(f[i - 1][j - 1] if j - 1 >= 0 else 0, f[i - 1][j] if j < m else 0, f[i - 1][j + 1] if j + 1 < m else 0)
    ans = 0
    for i in range(n):
        for j in range(m):
            if f[i][j] % k == 0:
                ans = max(ans, f[i][j])
    print(ans)

if __name__ == '__main__':
    main()