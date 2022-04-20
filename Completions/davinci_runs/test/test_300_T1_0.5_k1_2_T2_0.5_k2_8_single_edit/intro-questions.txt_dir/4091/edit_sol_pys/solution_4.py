

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], a[i - 1])
    ans = 0  # 全体の最大値
    for i in range(k, n + 1):
        ans += dp[i - k]  # 最大値をk個ずつ足していく
    print(ans)  # 全体の最大値を出力
    i = 0  # 全体の最大値を求めるときのループ変数
    while i < n:  # 最後まで続ける
        j = i + k  # jは最大値を求めるときのループ変数
        if j > n:  # jがnを超えたらnにする
            j = n
        while j > i and dp[i] == dp[j]:  # dp[i]とdp[j]が等しくなるまで続ける
            j -= 1  # jを減らす
        print(j - i, end=" ")  # 最大値を出力
        i = j  # iをjにする
    print()  # 改行


main()
