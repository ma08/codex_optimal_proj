
def main():
    n, k = map(int, input().split())  # n:文字数, k:文字列の数
    s = input()  # 入力文字列
    dp = [0] * (n + 1)  # dp[i]は文字列sのi文字目までで、最大で何文字列作れるか
    for i in range(1, n + 1):  # i文字目まででの最大文字列数を求める
        for j in range(i):  # i文字目までの文字列を作る場合は、j文字目までの文字列を作って、そこからi文字目までの文字列を作る
            if s[j:i] in s:  # j文字目からi文字目までの文字列がsに含まれていたら
                dp[i] = max(dp[i], dp[j] + n - i + j)  # dp[i]を更新する
    if dp[n] < k:  # 最大文字列数がkより小さい場合は、文字列を作れない
        print(-1)  # -1を出力
    else:  # 最大文字列数がk以上の場合は、作れる
        print(dp[n])  # 最大文字列数を出力

if __name__ == '__main__':
    main()
