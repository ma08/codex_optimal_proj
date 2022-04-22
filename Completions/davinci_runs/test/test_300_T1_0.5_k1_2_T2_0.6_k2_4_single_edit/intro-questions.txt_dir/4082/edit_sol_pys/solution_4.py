

def main():
    n = int(input())
    a = list(map(int, input().split()))  # ここで入力した値を整数のリストに変換
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1, n):
        if a[i] > a[i-1]:  # 直前の値より大きい場合は1を足していく
            dp[i] = dp[i-1] + 1
        else:  # 直前の値以下の場合は1にする
            dp[i] = 1
    ans = max(dp)  # 最初の一回目の計算での最大値を取得
    for i in range(1, n-1):
        if a[i-1] < a[i+1]:
            ans = max(ans, dp[i-1] + dp[i+1])
    print(ans)

if __name__ == '__main__':
    main()
