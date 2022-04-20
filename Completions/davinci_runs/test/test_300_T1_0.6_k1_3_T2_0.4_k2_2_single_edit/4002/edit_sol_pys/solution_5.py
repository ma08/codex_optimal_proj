

def main():
    n, m, k = map(int, input().split()) # n: 행, m: 열, k: 반시계방향 회전 횟수
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    dp = [[0 for i in range(k)] for j in range(m + 1)] # dp[i][j] : i번째 열까지 반시계방향으로 j번 회전한 상태에서 얻을 수 있는 최대 합
    for i in range(1, m + 1): # i번째 열
        for j in range(k): # 반시계방향 회전 횟수
            for r in range(n): # 행
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + matrix[r][i - 1]) # 이전 열의 최대 합에 현재 열의 합을 더함
                dp[i][(j - matrix[r][i - 1]) % k] = max(dp[i][(j - matrix[r][i - 1]) % k], dp[i - 1][j] + matrix[r][i - 1]) # 이전 열의 최대 합에 현재 열의 합을 더하고 반시계방향 회전 횟수를 1 늘림
    print(max(dp[m][0], dp[m][k // 2])) # 마지막 열까지 반시계방향 회전 횟수가 0이거나 k // 2인 상태에서 얻을 수 있는 최대 합

if __name__ == "__main__":
    main()
