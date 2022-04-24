

def solve(n, m, p, x):
    dp = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n + 1):
            if p[j - 1] == m and j - i <= x:
                dp[j] += 1

    return sum(dp)


if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]  # 座席
    x = int(input())  # 連続する座席数

    print(solve(n, m, p, x))
