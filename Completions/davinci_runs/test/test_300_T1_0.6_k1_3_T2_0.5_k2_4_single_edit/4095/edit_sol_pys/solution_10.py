

def solve(n, p):
    dp = [0] * (n + 2)

    for i in range(n):
        for j in range(i + 1, n + 2):
            if p[j - 1] == p[i]:
                dp[j] += 1

    return sum(dp)


if __name__ == "__main__":
    n = int(input())
    p = [int(i) for i in input().split()]

    print(solve(n, p))
