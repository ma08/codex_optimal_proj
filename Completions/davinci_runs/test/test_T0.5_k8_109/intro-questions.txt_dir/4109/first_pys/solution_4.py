

def solve(N, M, A, C):
    # dp[i][j] := i番目までの本を読んで、j番目のアルゴリズムの理解度がX以上になるときの最小費用
    dp = [[float("inf")] * (M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M+1):
            # i番目の本を読まない場合
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            # i番目の本を読む場合
            for k in range(j, M+1):
                dp[i+1][k] = min(dp[i+1][k], dp[i][j] + C[i])
    ans = float("inf")
    for i in range(M+1):
        if dp[N][i] != float("inf"):
            ans = min(ans, dp[N][i])
    return ans if ans != float("inf") else -1



if __name__ == "__main__":
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    C = list(map(int, input().split()))
    print(solve(N, M, A, C))