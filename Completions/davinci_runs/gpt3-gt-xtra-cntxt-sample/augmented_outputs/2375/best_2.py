def threeBlockPalindrome(a):
    n = len(a)
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[i][i] = 1
    for i in range(n-1):
        if a[i] == a[i+1]:
            f[i][i+1] = 2
        else:
            f[i][i+1] = 1
    for l in range(3, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if a[i] == a[j]:
                f[i][j] = f[i+1][j-1] + 2
            else:
                f[i][j] = max(f[i+1][j], f[i][j-1], f[i+1][j-1])
    return f[0][n-1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(threeBlockPalindrome(a))